# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from time import sleep


class WangyiproDownloaderMiddleware:

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None
        # 拦截五大板块对应的相应对象,进行篡改

    def process_response(self, request, response, spider):
        bro = spider.bro  # 获取浏览器对象
        # url -> request -> response
        if request.url in spider.models_urls:
            bro.get(request.url)
            sleep(2)
            page_text = bro.page_source
            # 五大板块对应的响应对象 针对定位到的这些response进行篡改,实例化一个新的响应对象 ,替代原来的响应对象
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response
        else:
            # 其他请求对应的响应对象
            return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
