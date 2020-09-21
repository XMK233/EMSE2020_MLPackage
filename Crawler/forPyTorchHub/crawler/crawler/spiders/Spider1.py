# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import scrapy, json, re, sys, time
from items import FilterItem

class PTHubSpiderFilterInfo(Spider):
    name = "PyTorchHubSpider_FilterInfo"
    start_urls = [
        "https://pytorch.org/hub/research-models/"
    ]
    xpaths = {
        "hub_filter_menu":
            "//div[@class='hub-filter-menu']//li/a/@data-tag",
        "get_module_names":
            "//div[@class='hub-card-title-container']/h4/text()",
        "next":
            "//li[@class='page-item']/a[text()='Next']/@href",   ## "//a[@class='page-link']",  ## //a[contains(text(),'Next')]/@href
    }

    custom_settings = {
        'ITEM_PIPELINES': {
            'crawler.pipelines.CrawlerPipeline_Filter': 200,
        }
    }

    def parse(self, response):
        filters = response.xpath(self.xpaths["hub_filter_menu"]).extract()
        for filter in filters:
            url = self.start_urls[0] + "{}/".format(filter)
            yield scrapy.Request(url,
                                 meta={"filter": filter,
                                       "modules": []},
                                 callback=self.next_page)

    def next_page(self, response):
        filter = response.meta["filter"]
        modules = response.meta["modules"]
        modules.extend(response.xpath(self.xpaths["get_module_names"]).extract())
        next_page_url = response.xpath(self.xpaths["next"]).extract_first()
        if next_page_url != None:
            yield scrapy.Request(
                "https://pytorch.org" + next_page_url,
                meta={"filter": filter,
                      "modules": modules},
                callback=self.next_page
            )
        else:
            item = FilterItem()
            item["filter"] = filter
            item["modules"] = modules
            yield item