# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json, os, scrapy, shutil
from settings import DATA_STORE
from scrapy.exporters import JsonItemExporter
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings
from items import FilterItem, HTMLItem, ModuleLinkItem, MetaInfoItem

data_directory = DATA_STORE
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

class CrawlerPipeline_MetaInfo(object):
    write_number = 0
    file_num = 0

    file = None
    exporter = None
    tmp_name = "tmp.json"

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

        f = open(os.path.join(data_directory, self.tmp_name), 'r', encoding="utf-8")
        text = f.read()
        f.close()

        data = json.loads(text)

        target_json = "meta_info.json"## spider.name + "_Info" + ".json"
        f = open(os.path.join(data_directory, target_json), 'w')
        json.dump(data, f, sort_keys=True, indent=4)
        f.close()

        self.file_num += 1

    def process_item(self, item, spider):
        if isinstance(item, MetaInfoItem):
            self.exporter.export_item(item)
            self.write_number += 1
        return item

class CrawlerPipeline_Filter(object):
    write_number = 0
    file_num = 0

    file = None
    exporter = None
    tmp_name = "tmp.json"

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

        f = open(os.path.join(data_directory, self.tmp_name), 'r', encoding="utf-8")
        text = f.read()
        f.close()

        data = json.loads(text)

        target_json = "filter.json" ## spider.name + "_Info" + ".json"
        f = open(os.path.join(data_directory, target_json), 'w')
        json.dump(data, f, sort_keys=True, indent=4)
        f.close()

        self.file_num += 1

    def process_item(self, item, spider):
        if isinstance(item, FilterItem):
            self.exporter.export_item(item)
            self.write_number += 1
        return item

class HTMLDownloadPipeline(FilesPipeline):
    # this pipeline can also download the notebooks.
    file_store = get_project_settings().get('FILES_STORE')
    def get_media_requests(self, item, info):
        if isinstance(item, HTMLItem):
            for url in item["HTML_urls"]:
                yield scrapy.Request(url)
        else:
            return
    def item_completed(self, results, item, info):
        if isinstance(item, HTMLItem):
            print(item)
            # 定义分类保存的路径
            img_path = os.path.join(self.file_store, item['modelName'])
            if os.path.exists(img_path) == False:
                os.makedirs(img_path)
            for i in range(len(results)):
                ok, x = results[i]
                if not ok:
                    _ = os.path.join(data_directory, "files/download_failed.csv")
                    with open(_, "a") as f:
                        f.write("{},{},{}\n".format(item["modelName"],
                                                    item["HTML_files"][i],
                                                    item["HTML_urls"][i]))
                    #continue
                else:
                    path = x["path"]
                    shutil.move(self.file_store + "/" + path,
                                img_path + "/" + item['HTML_files'][i])  # +image_paths[0]
                    pass
            return item
        return

class CrawlerPipeline_NameLink(object):
    write_number = 0
    file_num = 0

    file = None
    exporter = None
    tmp_name = "tmp.json"

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

        f = open(os.path.join(data_directory, self.tmp_name), 'r', encoding="utf-8")
        text = f.read()
        f.close()

        data = json.loads(text)

        target_json = "module_link.json"## spider.name + "_Info" + ".json"
        f = open(os.path.join(data_directory, target_json), 'w')
        json.dump(data, f, sort_keys=True, indent=4)
        f.close()

        self.file_num += 1

    def process_item(self, item, spider):
        if isinstance(item, ModuleLinkItem):
            self.exporter.export_item(item)
            self.write_number += 1
        return item