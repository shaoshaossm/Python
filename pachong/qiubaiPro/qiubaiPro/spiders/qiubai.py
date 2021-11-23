import scrapy
from qiubaiPro.items import QiubaiproItem


class FirstSpider(scrapy.Spider):
    # 爬虫文件名称
    name = 'qiubai'

    # 允许的域名
    # allowed_domains = ['www.xxx.com']
    # 起始url列表:存放的url会被scrapy自动进行请求的发送


    start_urls = ['https://www.qiushibaike.com/text/']
#
# def parse(self, response):
#     all_data = []
#     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
#
#     for div in div_list:
#         # extract: 将Selector对象中data参数存储的字符串提取出来
#         # author = div.xpath('./div[1]/a[2]/h2/text()')[0].extract() 作用一样 必须是一个列元素
#         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
#         content = div.xpath('./a[1]/div/span//text()').extract()
#         content = ''.join(content)
#         dic = {
#             'author': author,
#             'content': content
#         }
#         all_data.append(dic)
#         break
#     return all_data
    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')

        for div in div_list:
            # extract: 将Selector对象中data参数存储的字符串提取出来
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)
            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content
            yield item  # 将item提交给管道
