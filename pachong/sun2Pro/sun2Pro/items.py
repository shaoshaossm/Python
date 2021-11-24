# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Sun2ProItem(scrapy.Item):
    title = scrapy.Field()
    new_num = scrapy.Field()

