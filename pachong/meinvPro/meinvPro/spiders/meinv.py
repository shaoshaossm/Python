import scrapy
from meinvPro.items import MeinvproItem


class MeinvSpider(scrapy.Spider):
    name = 'meinv'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/index.html']
    url = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    page_num = 2

    def parse(self, response):

        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            img_name = li.xpath('./a/b/text()').extract_first()
            # 若有图片懒加载 使用伪属性
            img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src').extract_first()
            print(img_name, img_src)

            item = MeinvproItem()
            item['img_src'] = img_src
            yield item
        if self.page_num <= 10:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)
