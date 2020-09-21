# -*- coding: utf-8 -*-

# Scrapy settings for crawlerGlg project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawlerGlg'

SPIDER_MODULES = ['crawlerGlg.spiders']
NEWSPIDER_MODULE = 'crawlerGlg.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawlerGlg (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

IPPOOL = [
    {"ipaddr": "119.101.114.221:9999"},
    {"ipaddr": "111.181.36.60:9999"},
    {"ipaddr": "119.101.118.195:9999"},
    {"ipaddr": "115.151.2.147:9999"},
    {"ipaddr": "110.52.235.242:9999"},
    {"ipaddr": "116.31.2.91:8123"},
    {"ipaddr": "113.86.123.205:3128"},
    {"ipaddr": "61.187.240.7:3128"},
    {"ipaddr": "175.0.130.55:80"},
    {"ipaddr": "58.52.154.35:808"},
]
ROBOTSTXT_OBEY = True


class Proxies_Getter(object):
    """docstring for Proxies"""

    def __init__(self, verify=False):
        self.ips = []
        self.protocals = []
        self.ports = []
        self.proxies = []
        self.all_proxies = []
        self.headers = {
            'Accept': '*/*',
            'User-Agent': '"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        self.get_proxies()
        if verify:
            self.verify_proxies()

    def get_proxies(self):
        xpaths = {
            "ip":
                "//ul[@class='l2']/span[1]/li/text()",
            "port":
                "//ul[@class='l2']/span[2]/li/text()",
            "isHttps":
                "//ul[@class='l2']/span[4]/li/text()"
        }

        for t in ["gngn", "gnpt", "gwgn", "gwpt"]:
            print(t)
            url = "http://www.data5u.com/free/{}/index.shtml".format(t)
            #             html = webdriver.request('GET', url).content
            html = requests.get(url, headers=self.headers).content
            page_source = etree.HTML(html)
            self.ips.extend(page_source.xpath(xpaths["ip"]))
            self.ports.extend(page_source.xpath(xpaths["port"]))
            self.protocals.extend(page_source.xpath(xpaths["isHttps"]))

    def verify_proxies(self):
        print("start verifying...")
        for ip, port, isHttp in zip(self.ips, self.ports, self.protocals):
            protocol = isHttp
            proxy = "{}://{}:{}".format(isHttp, ip, port)
            proxies = {protocol: proxy}
            try:
                if requests.get('http://www.baidu.com', proxies=proxies, timeout=2).status_code == 200:
                    print('success %s' % proxy)
                    self.proxies.append({"ipaddr": proxy})
            except:
                print('fail %s' % proxy)
                # elf.failed_proxies.append({"ipaddr": proxy})
            self.all_proxies.append({"ipaddr": proxy})

IPPOOL = [
    {"ipaddr": "103.239.54.56:45462"},
    {"ipaddr": "195.206.34.238:31499"},
    {"ipaddr": "181.196.207.46:65238"},
]

import requests
from lxml import etree

# a = Proxies_Getter(True)
# IPPOOL = a.proxies if a.proxies != [] else a.all_proxies


USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]

DOWNLOAD_SLEEP_TIME = 1
#SPLIT_FILE =

def make_latest_storage(target_storage_dir):
    import os, re
    from datetime import datetime, timedelta
    latest_folder = None
    latest_date = None
    for _ in os.listdir(target_storage_dir):
        folder = os.path.join(target_storage_dir, _)
        if not os.path.isdir(folder):
            continue
        match = re.match(r"(\d{4}-\d{1,2}-\d{1,2})", _)
        # l = len(date_all)
        # if l <= 0:
        # 	continue
        if not match:
            continue
        latest_folder = folder
        latest_date = _

    # latest_time = datetime.strptime(latest_date, '%Y-%m-%d')
    # yes_time = latest_time + timedelta(days=7)
    # current_time = yes_time.strftime('%Y-%m-%d')
    # os.makedirs(os.path.join(target_storage_dir, current_time))

    latest_time = datetime.strptime(latest_date, '%Y-%m-%d')
    add_7_date = latest_time + timedelta(weeks=1)
    add_14_date = latest_time + timedelta(weeks=2)
    today = datetime.today()
    if today < add_7_date:
        current_time = latest_time.strftime('%Y-%m-%d')
    elif (today >= add_7_date) and (today < add_14_date):
        current_time = add_7_date.strftime('%Y-%m-%d')
        os.makedirs(os.path.join(target_storage_dir, current_time))
    else:
        # current_time = add_14_date.strftime('%Y-%m-%d')
        current_time = today.strftime('%Y-%m-%d')
        os.makedirs(os.path.join(target_storage_dir, current_time))
    return os.path.join(target_storage_dir, current_time)

DATA_STORE = make_latest_storage(r"J:\EMSE2020_MLPackage\Data\TFHub") # r"J:\CrawlerForModelStore\forAIHub\crawlerGlg\crawlerGlg\Data"
#SPLIT_DIR = "{}_webpages/".format(DIMENSION)
FILES_STORE = DATA_STORE # + SPLIT_DIR
DOWNLOAD_STORE = DATA_STORE #+ "/files"

#MAX_TO_WRITE_IN_A_FILE = 500

CHROME_PATH = "C:\\Users\\xmk233\\Downloads\\chromedriver.exe"
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

CONCURRENT_REQUESTS = 1
CONCURRENT_ITEMS = 1

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    # 'crawlerGlg.middlewares.IPPOOlS': 125,
    # 'crawlerGlg.middlewares.HeadlessGoogleMiddleware': 500,
    'crawlerGlg.middlewares.RandomUserAgentMiddleware': 400, # ä¿®æ”¹è¿™é‡Œçš„myspiderä¸ºé¡¹ç›®åç§°#'crawler.middlewares.ProxyMiddleware': 410, # åŒä¸Š
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': None
}

ITEM_PIPELINES = {
    # "crawlerGlg.pipelines.OverallDownloadPipeline": 2,
    "crawlerGlg.pipelines.EvolutionItemPipeline": 3,
    "crawlerGlg.pipelines.CrawlerPipeline_each_page": 4,
    "crawlerGlg.pipelines.OverallDownloadPipeline": 6,
    "crawlerGlg.pipelines.DoSomethingBeforeExit": 7,
}
