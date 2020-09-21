# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
import os, json, re, scrapy, shutil, time, tqdm
from scrapy.utils.project import get_project_settings
from settings import DATA_STORE, DOWNLOAD_STORE, FILES_STORE
from items import CrawlerglgItem, EvolutionRecordItem, DownloadHtml, CrawlerglgItemTFHub
#import wget

data_directory = DATA_STORE

class OverallDownloadPipeline(FilesPipeline):
    file_store = get_project_settings().get('FILES_STORE')
    page_store = get_project_settings().get('DOWNLOAD_STORE')
    sleep_time = get_project_settings().get('DOWNLOAD_SLEEP_TIME')
    def get_media_requests(self, item, info):
        if isinstance(item, DownloadHtml):
            print("in overall pipeline: ", type(item), item)
            # time.sleep(self.sleep_time)
            # yield scrapy.Request(item["file_url"])
            for url in tqdm.tqdm(item["file_url"]):
                time.sleep(self.sleep_time)
                yield scrapy.Request(url)
        else:
            return
    def item_completed(self, results, item, info):
        if isinstance(item, DownloadHtml):
            print("in overall pipeline: ", type(item), item)
            img_path = os.path.join(self.page_store, item['spider_name'], item["file_name"], "html") #
            if os.path.exists(img_path) == False:
                os.makedirs(img_path)
            for i in range(len(results)):
                ok, x = results[i]
                if not ok:
                    continue
                else:
                    print()
                    path = x["path"]
                    shutil.move(
                        os.path.join(self.file_store, path),
                        os.path.join(img_path, "{}.html".format(item['file_version'][i]))
                    )
                    print("page {} moved successfully".format(i))
            return item
        return

class DoSomethingBeforeExit(object):
    def close_spider(self, spider):
        with open("{}/last_id.csv".format(DATA_STORE), "w") as f:
            f.write("{},{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                   spider.last_model_version))

class CrawlerPipeline_each_page(object):
    write_number = 0
    file_num = 0

    file = None
    exporter = None
    tmp_name = "tmp_each_page.json"
    #tgt_name = "AIHubTFModule"

    def open_new_file(self):
        self.file = open(os.path.join(data_directory, self.tmp_name), 'wb')  # in some machines, we should use 'w'
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()
        return

    def __init__(self):
        self.open_new_file()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

        # if not (spider.name == "TFModuleSpider"):
        #     return

        f = open(os.path.join(data_directory, self.tmp_name), 'r', encoding="utf-8")
        text = f.read()
        f.close()

        data = json.loads(text)

        target_json = spider.name + "_Info" + ".json"
        f = open(os.path.join(data_directory, target_json), 'w')
        json.dump(data, f, sort_keys=True, indent=4)
        f.close()

        self.file_num += 1

    def process_item(self, item, spider):
        if isinstance(item, CrawlerglgItem) or isinstance(item, CrawlerglgItemTFHub):
            self.exporter.export_item(item)
            self.write_number += 1
        return item

class EvolutionItemPipeline(object):
    write_number = 0
    file_num = 0

    file = None
    exporter = None
    tmp_name = "tmp_evo.json"
    #tgt_name = "AIHubTFModule"

    def open_new_file(self):
        self.file = open(os.path.join(data_directory, self.tmp_name), 'wb')  # in some machines, we should use 'w'
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()
        return

    def __init__(self):
        self.open_new_file()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

        # if not (spider.name == "TFModuleSpider"):
        #     return

        f = open(os.path.join(data_directory, self.tmp_name), 'r', encoding="utf-8")
        text = f.read()
        f.close()

        data = json.loads(text)

        target_json = spider.name + "_Evo" + ".json"
        f = open(os.path.join(data_directory, target_json), 'w')
        json.dump(data, f, sort_keys=True, indent=4)
        f.close()

        self.file_num += 1

    def process_item(self, item, spider):
        if isinstance(item, EvolutionRecordItem):
            self.exporter.export_item(item)
            self.write_number += 1
        return item

