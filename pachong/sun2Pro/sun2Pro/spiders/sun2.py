import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from sun2Pro.items import Sun2ProItem
class Sun2Spider(RedisCrawlSpider):
    name = 'sun2'
    redis_key = 'sun'


    rules = (
        Rule(LinkExtractor(allow=r'id=2&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()
            item = Sun2ProItem()
            item['title'] = new_title
            item['new_num'] = new_num
            yield item

