import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redis import Redis
from moviePro.items import MovieproItem


class MovieSpider(CrawlSpider):
    name = 'movie'

    start_urls = ['http://www.male37.live/index.php/vod/type/id/2/page/2.html']

    rules = (
        # Rule(LinkExtractor(allow=r'/id/3/page/\d+/\.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'id/\d+/page/\d+\.html'), callback='parse_item', follow=True),
    )
    conn = Redis(host='127.0.0.1', port=6379)

    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[1]/div/div[1]/div/div/div[2]/ul/li')
        print(li_list)
        for li in li_list:
            detail_url = 'http://www.male37.live' + li.xpath('./div/a/@href').extract_first()
            ex = self.conn.sadd('urls', detail_url)
            if ex == 1:
                print('该url没有被爬取过,可以进行数据爬取!')
                yield scrapy.Request(url=detail_url, callback=self.parse_detail)
            else:
                print('数据还没更新,暂无新数据可爬取!')

    def parse_detail(self, response):
        item = MovieproItem()
        item['name'] = response.xpath(
            '/html/body/div[1]/div/div[1]/div[1]/div/div/div/div[2]/h1/text()').extract_first()
        print(item['name'], '--------------')
        item['desc'] = response.xpath(
            '/html/body/div[1]/div/div[1]/div[1]/div/div/div/div[2]/p[5]/span[2]').extract_first()
        item['desc'] = ''.join(item['desc'])
        yield item
