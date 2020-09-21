# -*- coding: utf-8 -*-
from scrapy import cmdline
#如果要把这些代码放到别的机子上跑，注意要改一些地址：
# data 的存储位置：pipelines
# file的存储地址: settings

# cmdline.execute('scrapy crawl TFModule'.split())
# cmdline.execute('scrapy crawl Notebook'.split())
# cmdline.execute('scrapy crawl Pipeline'.split())
# cmdline.execute('scrapy crawl Service'.split())
# cmdline.execute('scrapy crawl VMImage'.split())
# cmdline.execute('scrapy crawl TrainedModel'.split())
# cmdline.execute('scrapy crawl TechnicalGuide'.split())

# cmdline.execute('scrapy crawl TFHubModuleGoogle'.split())
cmdline.execute('scrapy crawl TFHubModule'.split())
# cmdline.execute('scrapy crawl TFHubModuleDeepMind'.split())


