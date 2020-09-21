# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
import scrapy, json, re, time
from items import CrawlerglgItem, EvolutionRecordItem, DownloadHtml, CrawlerglgItemTFHub

def model_name_legalization(string):
    return string.strip().replace("\\", "+").replace("/", "-").replace(":", "!").replace(">", "@") \
        .replace("*", "#").replace("?", "$").replace("\"", "%").replace("<", "^").replace("|", "&")
#####################################
####################################
class FirstPage(Spider):
    name = "AIHubSpider"
    index_of_payload = "TFModule"

    start_urls = [
        "https://aihub.cloud.google.com/s/list"
    ]
    payloads = {
        "TFModule": "[\"cma:po\",\"\",\"{}\",10,true,[[\"category\",[\"tensorflow-module\"]]],null,[],4,[]]",
        "Notebook": "[\"cma:po\",\"\",\"{}\",10,true,[[\"category\",[\"notebook\"]]],null,[],4,[]]",
        "Pipeline": "[\"cma:po\",\"\",\"{}\",10,true,[[\"category\",[\"pipeline\"]]],null,[],4,[]]",
        "Service": "[\"cma:po\",\"\",\"{}\",10,true,[[\"category\",[\"service\"]]],null,[],4,[]]",
        "VMImage": "[\"cma:po\",\"\",\"{}\",10,true,[[\"category\",[\"vm-image\"]]],null,[],4,[]]",
        "TrainedModel": "[\"cma:po\",\"\",\"{}\",10,true,[[\"category\",[\"trained-model\"]]],null,[],4,[]]",
        "TechnicalGuide": "[\"cma:po\",\"\",\"{}\",10,true,[[\"category\",[\"technical-guide\"]]],null,[],4,[]]",
    }
    headers = {
        'content-type': "application/json",
    }
    headers_each = {
        'content-type': "application/json; charset=utf-8",
    }
    last_model_version = ""

    def start_requests(self):
        # for pl in self.payloads:
        pl = self.payloads[self.index_of_payload]
        yield scrapy.Request(url= self.start_urls[0],
                             callback= self.parse,
                             method="POST",
                             #body= self.payload.format(""),
                             body= pl.format(""),
                             headers= self.headers,
                             meta= {"hehe": pl},
                             )

    def parse(self, response):
        # print("忠肝义胆 以身做盾 舍身无我 临危当先")
        pl = response.meta['hehe']
        heheda = json.loads(response.body[4:])[0]
        codes = heheda[1]
        meta_models = heheda[2]
        for meta_model in meta_models:
            name = model_name_legalization(meta_model[2])
            item_evo = EvolutionRecordItem()
            item_evo["name"] = name
            current_version = meta_model[11]
            if current_version != None:
                item_evo["cur_version"] = current_version
                yield item_evo
                for v in range(1, current_version + 1):
                    new_page_url = "https://aihub.cloud.google.com/p/products%2F{}/v/{}".format(meta_model[1].split("/")[1], v)
                    item_page = DownloadHtml()
                    item_page["file_name"] = name.replace(":", "|_|")
                    item_page['file_version'] = [v]
                    item_page['file_url'] = [new_page_url]
                    item_page['spider_name'] = self.name
                    yield item_page
                    ##################
                    new_url = "https://aihub.cloud.google.com/s/product/products%2F{}/version/{}".format(meta_model[1].split("/")[1], v)
                    time.sleep(1)
                    try:
                        yield scrapy.Request(
                            new_url,
                            meta={'model_name': name, "version": v, "payload": pl},
                            callback= self.each_page
                        )
                    except:
                        with open("fail.txt", "a") as f:
                            f.write("versioned yield failed: {} url: {}\n".format(name, new_url))
            else:
                new_page_url = "https://aihub.cloud.google.com/p/products%2F{}".format(meta_model[1].split("/")[1])
                item_page = DownloadHtml()
                item_page["file_name"] = name.replace(":", "%")
                item_page['file_version'] = [-1]
                item_page['file_url'] = [new_page_url]
                item_page['spider_name'] = self.name
                yield item_page
                ########################################
                item_evo["cur_version"] = -1
                yield item_evo
                new_url = "https://aihub.cloud.google.com/s/product/products%2F{}".format(meta_model[1].split("/")[1])
                #name
                time.sleep(1)
                try:
                    yield scrapy.Request(
                        new_url,
                        meta={'model_name': name, "version": -1, "payload": pl},
                        callback= self.each_page
                    )
                except:
                    with open("fail.txt", "a") as f:
                        f.write("unversioned yield failed: {}      url: {}\n".format(name, new_url))

        # time.sleep(1)
        yield scrapy.Request(
            self.start_urls[0],
             self.parse,
             method="POST",
             body= pl.format(codes), #self.payload.format(codes),
             headers= self.headers,
             meta= {"hehe": pl},
         )

    def each_page(self, response):
        model_name = response.meta['model_name']
        version = response.meta['version']
        payload = response.meta["payload"]
        heheda = json.loads(response.body[4:])[0]
        item_info = CrawlerglgItem()
        item_info["name"] = model_name
        item_info["version"] = version
        item_info["info"] = heheda
        print(payload)
        yield item_info
        self.last_model_version = "{},{},{},{}".format(response.url, model_name, version, payload)

    def each_version(self, response):
        pass

class TFModule(FirstPage):
    name = "TFModule"
    index_of_payload = "TFModule"

class Notebook(FirstPage):
    name = "Notebook"
    index_of_payload = "Notebook"

class Pipeline(FirstPage):
    name = "Pipeline"
    index_of_payload = "Pipeline"

class Service(FirstPage):
    name = "Service"
    index_of_payload = "Service"

class VMImage(FirstPage):
    name = "VMImage"
    index_of_payload = "VMImage"

class TrainedModel(FirstPage):
    name = "TrainedModel"
    index_of_payload = "TrainedModel"

class TechnicalGuide(FirstPage):
    name = "TechnicalGuide"
    index_of_payload = "TechnicalGuide"

class SecondPage(Spider):
    """
    This class is for original AIHub.
    Turned out that AIHub contains the TFHub products that published by Google and DeepMind.
    And there are 8 published on TFhub but not on AIHub. What are they?
    """
    name = "TFHubModule"
    index_of_payload = "TFHubModule"

    start_urls = [
        "https://tfhub.dev/s/list"
    ]
    payloads = {
        "TFHubModule": "[\"cma:po\", \"\", \"{}\", 100, true, [[\"subtype\", [\"module\", \"placeholder\"]]], null, [], null, []]",
        "TFHubModuleGoogle": "[\"cma:po\", \"\", \"{}\", 100, true, [[\"publisher\", [\"google\"]], [\"subtype\", [\"module\", \"placeholder\"]]], null, [], null, []]",
        "TFHubModuleDeepMind": "[\"cma:po\", \"\", \"{}\", 100, true, [[\"publisher\", [\"deepmind\"]], [\"subtype\", [\"module\", \"placeholder\"]]], null, [], null, []]",
    }
    headers = {
        'content-type': "application/json",
    }
    headers_each = {
        'content-type': "application/json; charset=utf-8",
    }
    last_model_version = ""

    def find_publisher(self, l):
        """
        :param l: is a list. No.42 element of the meta data
        :return: publisher name
        """
        for ll in l:
            if ll[0] == "publisher":
                return ll[1][0][0]
        return None

    def start_requests(self):
        # for pl in self.payloads:
        pl = self.payloads[self.index_of_payload]
        yield scrapy.Request(url= self.start_urls[0],
                             callback= self.parse,
                             method="POST",
                             #body= self.payload.format(""),
                             body= pl.format(""),
                             headers= self.headers,
                             meta= {"hehe": pl},
                             )

    def parse(self, response):
        # print("忠肝义胆 以身做盾 舍身无我 临危当先")
        pl = response.meta['hehe']
        heheda = json.loads(response.body[4:])[0]
        codes = heheda[1]
        meta_models = heheda[2]
        for meta_model in meta_models:
            publisher = self.find_publisher(meta_model[42])
            name = model_name_legalization(meta_model[2])
            item_evo = EvolutionRecordItem()
            item_evo["name"] = name
            current_version = meta_model[11]
            if current_version != None:
                item_evo["cur_version"] = current_version
                yield item_evo
                for v in range(1, current_version + 1):
                    new_page_url = "https://tfhub.dev/{}/{}/{}".format(publisher, meta_model[2], v) # "https://aihub.cloud.google.com/p/products%2F{}/v/{}".format(meta_model[1].split("/")[1], v)
                    item_page = DownloadHtml()
                    item_page["file_name"] = name.replace(":", "|_|")
                    item_page['file_version'] = [v]
                    item_page['file_url'] = [new_page_url]
                    item_page['spider_name'] = self.name
                    yield item_page
                    ##################
                    new_url = "https://tfhub.dev/s/lookup/1/{}/{}?version={}".format(publisher, meta_model[2].replace("/", "%2F"), v) ## "https://aihub.cloud.google.com/s/product/products%2F{}/version/{}".format(meta_model[1].split("/")[1], v)
                    time.sleep(1)
                    try:
                        yield scrapy.Request(
                            new_url,
                            meta={
                                'model_name': name,
                                "version": v,
                                "payload": pl,
                                # "publisher": publisher,
                                "URLTailPart": "{}/{}?version={}".format(publisher, meta_model[2].replace("/", "%2F"), v)
                            },
                            callback= self.each_page_TFHub_LV1 # self.each_page
                        )
                    except:
                        with open("fail.txt", "a") as f:
                            f.write("versioned yield failed: {} url: {}\n".format(name, new_url))
            else:
                new_page_url = "https://tfhub.dev/{}/{}".format(publisher, meta_model[2]) # new_page_url = "https://aihub.cloud.google.com/p/products%2F{}".format(meta_model[1].split("/")[1])
                item_page = DownloadHtml()
                item_page["file_name"] = name.replace(":", "%")
                item_page['file_version'] = [-1]
                item_page['file_url'] = [new_page_url]
                item_page['spider_name'] = self.name
                yield item_page
                ########################################
                item_evo["cur_version"] = -1
                yield item_evo
                new_url = "https://tfhub.dev/s/lookup/1/{}/{}".format(publisher,
                                                                                 meta_model[2].replace("/", "%2F")) # new_url = "https://aihub.cloud.google.com/s/product/products%2F{}".format(meta_model[1].split("/")[1])
                #name
                time.sleep(1)
                try:
                    yield scrapy.Request(
                        new_url,
                        meta={
                            'model_name': name,
                            "version": -1,
                            "payload": pl,
                            # "publisher": publisher,
                            "URLTailPart": "{}/{}".format(publisher,meta_model[2].replace("/", "%2F"))
                        },
                        callback= self.each_page_TFHub_LV1 ## self.each_page
                    )
                except:
                    with open("fail.txt", "a") as f:
                        f.write("unversioned yield failed: {}      url: {}\n".format(name, new_url))
        # time.sleep(1)
        yield scrapy.Request(
            self.start_urls[0],
             self.parse,
             method="POST",
             body= pl.format(codes.replace("\"", "\\\"")), ## codes #self.payload.format(codes),
             headers= self.headers,
             meta= {"hehe": pl},
         )
    def each_page_TFHub_LV1(self, response):
        model_name = response.meta['model_name']
        version = response.meta['version']
        payload = response.meta["payload"]
        urlTailPart = response.meta["URLTailPart"]
        ##
        metaData_lv1 = json.loads(response.body[4:])[0]
        ##
        new_url = "https://tfhub.dev/s/listModelFormats/{}".format(urlTailPart)
        ##
        yield scrapy.Request(
            new_url,
            meta={'model_name': model_name, "version": version, "info_NormalDeployment": metaData_lv1,"payload": payload},
            callback=self.each_page_TFHub_LV2  ## self.each_page
        )

    def each_page_TFHub_LV2(self, response):
        model_name = response.meta['model_name']
        version = response.meta['version']
        payload = response.meta["payload"]
        info_NormalDeployment = response.meta["info_NormalDeployment"]
        info_OtherDeployment = json.loads(response.body[4:])[0]
        item_info = CrawlerglgItemTFHub()
        item_info["name"] = model_name
        item_info["version"] = version
        item_info["info_NormalDeployment"] = info_NormalDeployment
        item_info["info_OtherDeployment"] = info_OtherDeployment
        ###
        yield item_info
        self.last_model_version = "{},{},{},{}".format(response.url, model_name, version, payload)


    # def each_page(self, response):
    #     model_name = response.meta['model_name']
    #     version = response.meta['version']
    #     payload = response.meta["payload"]
    #     heheda = json.loads(response.body[4:])[0]
    #     item_info = CrawlerglgItem()
    #     item_info["name"] = model_name
    #     item_info["version"] = version
    #     item_info["info"] = heheda
    #     # print(payload)
    #     yield item_info
    #     self.last_model_version = "{},{},{},{}".format(response.url, model_name, version, payload)

    def each_version(self, response):
        pass

class TFHubModuleGoogle(SecondPage):
    name = "TFHubModuleGoogle"
    index_of_payload = "TFHubModuleGoogle"

class TFHubModuleDeepMind(SecondPage):
    name = "TFHubModuleDeepMind"
    index_of_payload = "TFHubModuleDeepMind"