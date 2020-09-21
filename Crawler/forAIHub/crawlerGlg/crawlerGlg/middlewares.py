# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium.webdriver.chrome.options import Options
from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
import random
from scrapy.conf import settings
from scrapy import log
from settings import IPPOOL
from scrapy.utils.project import get_project_settings
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

chromedriver_path = settings.get("CHROME_PATH")

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = get_project_settings().get('USER_AGENT_LIST') #random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)
            #this is just to check which user agent is being used for request
            spider.log(
                u'User-Agent: {} {}'.format(request.headers.get('User-Agent'), request),
                level=log.DEBUG
            )

# class ProxyMiddleware(object):
#     def process_request(self, request, spider):
#         request.meta['proxy'] = settings.get('HTTP_PROXY')

class IPPOOlS(HttpProxyMiddleware):
    # 初始化
    def __init__(self, ip=''):
        # self.IPPool = get_project_settings().get('IPPOOL')
        # print(self.IPPool)
        self.ip = ip
    # 請求處理
    def process_request(self, request, spider):
        # 先隨機選擇一個IP
        thisip = random.choice(IPPOOL)
        print("當前使用IP是："+ thisip["ipaddr"])
        request.meta["proxy"] = thisip["ipaddr"] #"http://"+

# class JavaScriptMiddleware(object):
#
#     def __init__(self):
#         self.browser = webdriver.PhantomJS(executable_path=browser_executable_path)
#         super(JavaScriptMiddleware, self).__init__()
#
#         from scrapy.xlib.pydispatch import dispatcher
#         from scrapy import signals
#         dispatcher.connect(self.spider_closed, signals.spider_closed)
#
#         return
#
#     def spider_closed(self, spider):
#         print ('spider closed')
#         self.browser.quit()
#         return
#
#     def process_request(self, request, spider):
#
#         if True:
#             print ("PhantomJS is starting...")
#             # driver = webdriver.Firefox()
#             self.browser.get(request.url)
#             time.sleep(1)
#             body = self.browser.page_source
#             print ("Calling " + request.url)
#             return HtmlResponse(self.browser.current_url, body=body, encoding='utf-8', request=request)
#         else:
#             return

class HeadlessGoogleMiddleware(object):
# 原文：https://blog.csdn.net/lilongsy/article/details/80531378
    driver = None
    req_count = 0
    req_limit = 20
    def __init__(self):
        self.open_driver()

    def process_request(self, request, spider):
        self.driver.get(request.url)
        print("浓墨饱蘸绛唇点。。。")
        self.driver.execute_script("scroll(0, 1000);")
        time.sleep(1)
        rendered_body = self.driver.page_source
        print("点睛笔歇神自来。。。")
        _ = HtmlResponse(request.url, body=rendered_body, encoding="utf-8")
        self.req_count += 1
        print("request count: ", self.req_count)
        if self.req_count >= self.req_limit:
            self.req_count = 0
            print("酒席散尽人不寐")
            self.close_driver()
            #time.sleep(60)
            print("念念不忘终复还")
            self.open_driver()
        return _

    def spider_closed(self, spider, reason):
        print('一轮弯月，一剑西来，一声笑傲，一路平安')
        self.close_driver()

    def close_driver(self):
        self.driver.close()

    def open_driver(self):
        option = Options()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path= chromedriver_path,
                                       chrome_options=option)