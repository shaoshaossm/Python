import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem,DetailItem

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=2&page=2']
    link = LinkExtractor(allow=r'id=2&page=\d+')

    # link_detail = 'https://wz.sun0769.com/political/politics/index?' + LinkExtractor(allow=r'id=\d+')
    link_detail = LinkExtractor(allow=r'id=\d+')
    print(link_detail)
    rules = (
        # LinkExtractor 链接提取器
        # allows = (正则) 根据指定规则进行链接提取
        # follow=True : 将链接提取器继续作用到链接提取器提取到的链接所对应的页面中
        # 规则解析器 : 将链接提取提取到的链接进行指定规则 (callback) 的解析操作

        Rule(link, callback='parse_item', follow=True),
        Rule(link_detail, callback='parse_detail')

    )

    # 解析新闻编号、标题
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()
            item = SunproItem()
            item['title'] = new_title
            item['new_num'] = new_num
            yield item

    # 解析新闻内容、编号
    def parse_detail(self, response):
        new_id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        new_content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        new_content = ''.join(new_content)
        item = DetailItem()
        item['new_id'] = new_id
        item['content'] = new_content
        print(new_id,new_content)
        yield item
