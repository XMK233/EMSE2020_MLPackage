# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MetaInfoItem(scrapy.Item):
    modelName = scrapy.Field()
    modelURL = scrapy.Field()
    dataTag = scrapy.Field()
    pass

class HTMLItem(scrapy.Item):
    modelName = scrapy.Field()
    HTML_files = scrapy.Field()
    HTML_urls = scrapy.Field()
    # modelURL = scrapy.Field()
    # scriptURL = scrapy.Field()
    pass

class ModuleLinkItem(scrapy.Item):
    module = scrapy.Field()
    link = scrapy.Field()
    pass

class FilterItem(scrapy.Item):
    filter = scrapy.Field()
    modules = scrapy.Field()
    pass

class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


