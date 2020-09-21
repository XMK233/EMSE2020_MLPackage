# -*- coding: utf-8 -*-
from scrapy import cmdline
import re, json, wget

# cmdline.execute('scrapy crawl PyTorchHubSpider_FilterInfo'.split())
# cmdline.execute('scrapy crawl PyTorchHubSpider_ModuleInfo'.split())

cmdline.execute('scrapy crawl Spider_ModelZoo'.split())