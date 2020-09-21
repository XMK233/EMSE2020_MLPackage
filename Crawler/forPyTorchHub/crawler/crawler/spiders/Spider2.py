# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import scrapy, json, re, sys, time
from items import ModuleLinkItem, HTMLItem

class PTHubSpiderModuleInfo(Spider):
    name = "PyTorchHubSpider_ModuleInfo"
    start_urls = [
        "https://pytorch.org/hub/research-models/"
    ]
    xpaths = {
        "hub_filter_menu":
            "//div[@class='hub-filter-menu']//li/a/@data-tag",
        "get_module_names":
            "//div[@class='hub-card-title-container']/h4/text()",
        "module_url":
            "//div[@class='card hub-card']/a/@href",
        "next":
            "//li[@class='page-item']/a[text()='Next']/@href",   ## "//a[@class='page-link']",  ## //a[contains(text(),'Next')]/@href
    }

    custom_settings = {
        'ITEM_PIPELINES': {
            'crawler.pipelines.HTMLDownloadPipeline': 2,
            'crawler.pipelines.CrawlerPipeline_NameLink': 1,
        }
    }

    def parse(self, response):
        module_urls = response.xpath(self.xpaths["module_url"]).extract()
        module_names = response.xpath(self.xpaths["get_module_names"]).extract()

        for module_url, module_name in zip(module_urls, module_names):
            yield scrapy.Request(
                "https://pytorch.org" + module_url,
                meta={"module": module_name},
                callback=self.each_page
            )

        next_page_url = response.xpath(self.xpaths["next"]).extract_first()
        if next_page_url != None:
            yield scrapy.Request(
                "https://pytorch.org" + next_page_url,
                # meta={ },
                callback=self.parse
            )
        else:
           pass

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