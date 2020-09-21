import torch, os, shutil, re, time, json
from lxml import etree
import torch

DATA_DIR = r"J:\ModelStoreData\PyTorchHub\2019-07-30"
TARGET_DIR = os.path.join(DATA_DIR, "files")
CKPT_DIR = r"C:\Users\xmk233\.cache\torch\checkpoints"
FILE_DIR = TARGET_DIR
PYTORCH_TRANSFORMER_DIR = r"C:\Users\xmk233\.cache\torch\pytorch_transformers"
record_file_path = os.path.join(DATA_DIR, "record.json")

def download_all_of_the_modules():
    module_info = {}

    def download_files(module, ckpt_dir, dir, repo, entrypoint, *args, **kargs):
        entrypoint = entrypoint.replace("'", "")
        torch.hub.set_dir(
            os.path.join(dir)
        )

        print("\n\n\n\n\n {}, {}, {}".format(repo, entrypoint, dir))
        if len(kargs) == 0 and len(args) == 0:
            cmd = "torch.hub.load('{}', '{}')".format(repo, entrypoint)
        elif len(args) != 0:
            cmd = "torch.hub.load('{}', '{}', {})".format(repo, entrypoint, ", ".join(args))
        elif len(kargs) != 0:
            params = []
            for k, v in kargs.items():
                params.append("{}={}".format(k, v))
            cmd = "torch.hub.load('{}', '{}', {})".format(repo, entrypoint, ", ".join(params))  # , pretrained=True
        print(cmd)
        a = eval(cmd)
        module_info["{}___{}___{}".format(module, repo, entrypoint)] = str(a)
        time.sleep(1)
        for ckpt in os.listdir(ckpt_dir):
            shutil.move(
                os.path.join(ckpt_dir, ckpt),
                os.path.join(dir, "{}__{}".format(entrypoint, ckpt))
            )

    def find_repo_from_items(items):
        for item in items:
            if len(item.split("/")) == 2:
                return items.index(item)

    file_dir = FILE_DIR

    for module in os.listdir(file_dir):
        if module == ".ipynb_checkpoints":
            continue

        module_dir = os.path.join(file_dir, module)
        html_path = os.path.join(module_dir, "webpage.html")
        with open(html_path, "r", encoding="utf-8") as hp:
            html = hp.read()
        page_source = etree.HTML(html)
        module_author = page_source.xpath('//p[@class="detail-lead"]/text()')[0]
        items = page_source.xpath("//code/span[@class='s']/text()")
        repo_index = find_repo_from_items(items)
        repo = items[repo_index]
        repo = repo.replace("'", "").replace("\"", "")

        if ("Pytorch Team" in module_author) or (
                "Facebook AI" in module_author):  ### Pytorch Team模型和Facebook AI模型：找//table/tbody/tr/td[1]
            # continue ### SCALE02
            if module == "ResNext WSL":
                eps = [
                    "resnext101_32x8d_wsl",
                    "resnext101_32x16d_wsl",
                    "resnext101_32x32d_wsl",
                    "resnext101_32x48d_wsl",
                ]
                for ep in eps:
                    download_files(
                        module,
                        CKPT_DIR,
                        os.path.join(TARGET_DIR, module),
                        repo,
                        ep
                    )
            elif module == "ShuffleNet v2":
                eps = ["shufflenet_v2_x1_0"]
                for ep in eps:
                    download_files(
                        module,
                        CKPT_DIR,
                        os.path.join(TARGET_DIR, module),
                        repo,
                        ep,
                        pretrained="True"
                    )
            else:
                eps = page_source.xpath('//table/tbody/tr/td[1]/text()')
                for ep in eps:
                    download_files(
                        module,
                        CKPT_DIR,
                        os.path.join(TARGET_DIR, module),
                        repo,
                        ep,
                        pretrained="True"
                    )
            break
        elif "HuggingFace Team" in module_author:  ### HuggingFace Team模型： 在module description和 requirement之间的部分，找//code[@class="highlighter-rouge"]/text()
            continue  ### SCALE02 4 modules.
            torch.hub.set_dir(
                os.path.join(TARGET_DIR, module)
            )
            _ = re.findall('<article class="pytorch-article">([\s\S]*)<h3 id="requirements">', html)[0]  #
            eps = etree.HTML(_).xpath('//code[@class="highlighter-rouge"]/text()')
            for ep in eps:
                download_files(
                    module,
                    PYTORCH_TRANSFORMER_DIR,
                    os.path.join(TARGET_DIR, module),
                    repo,
                    ep,
                    "bert-base-cased" if module == "BERT" else
                        "transfo-xl-wt103" if module == "Transformer-XL" else
                        "gpt2" if module == "GPT-2" else
                        "openai-gpt", # when module == "GPT"
                )
        #                 cmd = "torch.hub.load('{}', '{}', '{}')".format(
        #                             repo,
        #                             ep.replace("'", ""),
        #                             "bert-base-cased" if module == "BERT" else
        #                                 "transfo-xl-wt103" if module == "Transformer-XL" else
        #                                 "gpt2" if module == "GPT-2" else
        #                                 "openai-gpt" # when module == "GPT"
        #                         )
        #                 try:
        #                     print("\n\n\n\n\n {}, '{}'...{}".format(repo, ep.replace("'", ""), module_dir))
        #                     a = eval(cmd)
        #                     module_info["{}___{}___{}".format(module, repo, ep)] = str(a)
        #                 except:
        #                     print("xxxxxxxxxxxxx failed", module, cmd)
        #                 time.sleep(1)
        #                 for ckpt in os.listdir(ckpt_dir):
        #                     shutil.move(
        #                         os.path.join(ckpt_dir, ckpt),
        #                         os.path.join(module_dir, "{}__{}".format(ep, ckpt))
        #                     )

        else:  ### NVIDIA, FAIR HDGAN, 以及个人发布的模型，都在这里处理了。
            continue  ### COLAB. 6 modules.
            eps = [items[repo_index + 1]]
            for ep in eps:
                download_files(
                    module,
                    CKPT_DIR,
                    os.path.join(TARGET_DIR, module),
                    repo,
                    ep
                )
            ### these code is used to zip the files on colab. After zipping, we can download the zipped files.
    #             formalize_module_dir = module_dir.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)")
    #             shell = "zip -r {}.zip {}".format(formalize_module_dir, formalize_module_dir)
    #             print(shell)
    #             os.system(shell)
    with open(record_file_path, "a") as rfp:
        json.dump(module_info, rfp, indent=4, sort_keys=True)


download_all_of_the_modules()