# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import scrapy, json, re, sys, time
from items import MetaInfoItem, ModuleLinkItem, HTMLItem

class PTHubSpiderMetaInfo(Spider):
    name = "PyTorchHubSpider_MetaInfo"
    start_urls = [
        "https://pytorch.org/hub/research-models"
    ]
    xpaths = {
        "data_tags":
            "//div[@class='col-md-6 research-hub-card-wrapper']/@data-tags",
        "urls":
            "//div[@class='col-md-6 research-hub-card-wrapper']//a/@href",
        "names":
            "//li[@class='card-title']/text()",
    }

    custom_settings = {
        'ITEM_PIPELINES': {
            'crawler.pipelines.CrawlerPipeline_MetaInfo': 1,
            'crawler.pipelines.HTMLDownloadPipeline': 3,
            # 'crawler.pipelines.CrawlerPipeline_NameLink': 2,
        }
    }

    def parse(self, response):
        data_tags = response.xpath(self.xpaths["data_tags"]).extract()
        urls = response.xpath(self.xpaths["urls"]).extract()
        names = response.xpath(self.xpaths["names"]).extract()
        for data_tag, url, name in zip(data_tags, urls, names):
            metainfoitem = MetaInfoItem()
            metainfoitem["dataTag"] = data_tag
            metainfoitem["modelURL"] = url
            metainfoitem["modelName"] = name
            yield metainfoitem

            yield scrapy.Request(
                "https://pytorch.org" + url,
                meta={"module": name},
                callback=self.each_page
            )

    def each_page(self, response):
        module = response.meta["module"]
        ##
        modulelink_item = ModuleLinkItem()
        modulelink_item["module"] = module
        modulelink_item["link"] = response.url
        yield modulelink_item
        # print(module, response.url)
        item_html = HTMLItem()
        item_html["modelName"] = module
        item_html["HTML_files"] = ["webpage.html"]
        item_html["HTML_urls"] = [response.url]
        yield item_html