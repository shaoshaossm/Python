# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

import random
class MiddleproSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MiddleproDownloaderMiddleware:
    # UA伪装
    user_agent_list=[
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    ]
    # 代理池
    PROXY_http = [
        '153.180.102.104:80',
        '195.208.131.189:56055'
    ]
    PROXY_https = [
        '120.83.49.90.9000',
        '95.189.112.214:35508'
    ]



    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        # 方便测试
        request.meta['proxy'] = 'http://58.209.234.8:58.209.234.8'

        return None

    def process_response(self, request, response, spider):

        return response

    def process_exception(self, request, exception, spider):
        # 代理
        if request.url.split(':')[0] == 'http':
            request.meta['proxy'] = 'http://'+random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'https://'+random.choice(self.PROXY_https)
        return request # 将修正后的请求对象进行重新发送

