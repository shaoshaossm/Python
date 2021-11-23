import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件名称
    name = 'first'
    # 允许的域名
    # allowed_domains = ['www.xxx.com']
    # 起始url列表:存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://www.baidu.com/', 'https://www.sogou.com/']

    def parse(self, response):
        print(response)
