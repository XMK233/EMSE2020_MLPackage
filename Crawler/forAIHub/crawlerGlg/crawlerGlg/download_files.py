import json, os, wget, tqdm, requests, time, shutil
# from selenium import webdriver
from settings import DOWNLOAD_STORE, CHROME_PATH

download_store = DOWNLOAD_STORE


def download_files_Pipeline():
    asset_type = "Pipeline"
    with open(os.path.join(download_store, "{}_Info.json".format(asset_type))) as at:
        items = json.load(at)
    for item in tqdm.tqdm(items):
        name = item["name"]
        version = item["version"]
        file_link = (item["info"][1][9])
        file_name = file_link.split("/")[-1]
        file_dir = os.path.join(download_store, asset_type, name, "file")
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        # new_file_path = os.path.join(file_dir, f"{version}_{file_name}")
        downloaded_file_name = wget.download(file_link)
        shutil.move(
            downloaded_file_name,
            os.path.join(file_dir, f"{version}_{downloaded_file_name}")
        )


# download_files_Pipeline()


def transform_md_to_Notebooks():
    asset_type = "Notebook"
    with open(os.path.join(download_store, "{}_Info.json".format(asset_type))) as at:
        items = json.load(at)
    for item in tqdm.tqdm(items):
        name = item["name"]
        version = item["version"]

        #         if item["info"][1][9] == None and item["info"][1][10] != None:
        #             file_link = item["info"][1][10]
        #         elif item["info"][1][10] == None and item["info"][1][9] != None:
        #             file_link = item["info"][1][9]
        #         else:
        #             file_link = "xx/(NameUnknown).ipynb"

        #         if file_link == None:
        #             print(name)
        #         file_name = file_link.split("/")[-1]

        #         if "?" in file_name:
        #             file_name = file_name.split("?")[0]

        # file_name = f"{version}_{file_link}.ipynb"

        file_dir = os.path.join(download_store, asset_type, name, "file")
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        # new_file_path = os.path.join(file_dir, file_name)
        new_file_path = os.path.join(file_dir, f"{version}.ipynb")  # f"{version}_{file_name}"

        content = item["info"][1][7]
        #         if name != "Text generation using a RNN with eager execution":
        #             continue
        with open("input.md", "w", encoding="utf-8") as f:
            #             print(content)
            f.write(content)  # .replace("\\n", "\n").replace("\\\"", "\"")
        os.system("notedown input.md > output.ipynb")
        shutil.move("output.ipynb", new_file_path)
    os.remove("input.md")


# transform_md_to_Notebooks()

def download_models_for_TFModule():
    import tensorflow_hub as hub
    asset_type = "TFModule"
    with open(os.path.join(download_store, "{}_Info.json".format(asset_type))) as at:
        items = json.load(at)
    for item in tqdm.tqdm(items):
        name = item["name"]
        version = item["version"]
        file_link = item["info"][1][9]

        file_dir = os.path.join(download_store, asset_type, name, "file", f"{version}")
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        os.environ["TFHUB_CACHE_DIR"] = file_dir

        m = hub.Module(file_link)
        ### if you want to export the module, you can export the "m" in a session
        ### but this is not necessary.
        # with tf.Session() as sess:
        #     sess.run(tf.global_variables_initializer())
        #     m.export("heheda", sess)

download_models_for_TFModule()