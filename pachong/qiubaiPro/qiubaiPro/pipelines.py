# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql


class QiubaiproPipeline:
    fp = None

    # 重写父类的方法,该方法只在爬虫时调用一次
    def open_spider(self, spider):
        self.fp = open('./qiubai.txt', 'w', encoding='utf-8')

    # 接受爬虫过来的item对象,处理item类型的对象,每接收一个item对象调用一次
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author + ':' + content + '\n')
        return item  # 就会传递给下一个即将被执行的管道类

    # 重写父类的方法,该方法只在爬虫结束调用一次
    def close_spider(self, spider):
        print('结束爬虫!')
        self.fp.close()


# 管道文件中一个管道类对应一组数据存储到一个平台或者载体中
class mysqlPileLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='hxl158120', db='qiubai',
                                    charset='utf8')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute('insert into qiubai values("%s","%s")' % (item["author"], item["content"]))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
