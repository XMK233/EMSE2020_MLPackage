# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DownloadHtml(scrapy.Item):
    file_name = scrapy.Field()
    file_version = scrapy.Field()
    file_url = scrapy.Field()
    files = scrapy.Field()
    spider_name = scrapy.Field()
    pass

class CrawlerglgItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    version = scrapy.Field()
    info = scrapy.Field()
    pass

class CrawlerglgItemTFHub(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    version = scrapy.Field()
    info_NormalDeployment = scrapy.Field()
    info_OtherDeployment = scrapy.Field()
    pass

class EvolutionRecordItem(scrapy.Item):
    name = scrapy.Field()
    cur_version = scrapy.Field()
    pass
