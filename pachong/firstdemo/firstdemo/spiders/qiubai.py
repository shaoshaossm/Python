import scrapy


class FirstSpider(scrapy.Spider):
    # 爬虫文件名称
    name = 'qiubai'
    # 允许的域名
    # allowed_domains = ['www.xxx.com']
    # 起始url列表:存放的url会被scrapy自动进行请求的发送
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')

        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()')[0]
            content = div.xpath('./a[1]/div/span//text()')
            print(author, content)
            print(author)
            break
