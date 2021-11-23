import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = []  # 存储板块对应详情页对应的url


    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='E:\PyCharm\pachong\com\ssm\seleniumTest\chromedriver.exe')

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        print(li_list)
        alist = [3, 4, 6, 7, 8]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)
        for url in self.models_urls:
            yield scrapy.Request(url, callback=self.parse_model)

    # 解析每个板块页面中对应新闻的标题和新闻详情页的url
    def parse_model(self, response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            print(title)
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            item = WangyiproItem()
            item['title'] = title

            # 对新闻详情页的url发起请求
            yield scrapy.Request(url=new_detail_url, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        all_data = []
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)

        item = response.meta['item']

        item['content'] = content
        dic = {
            'content': content
        }
        all_data.append(dic)
        yield item
        return all_data
    def closed(self, spider):
        self.bro.quit()
