import tensorflow as tf
import tensorflow_hub as hub
import os, json

PATH = r"J:\ModelStoreData\AIHub\2019-06-04\TFModule"

module_list = os.listdir(PATH)
### zheli
os.environ["TFHUB_CACHE_DIR"] = r"J:\CrawlerForModelStore\forAIHub\crawlerGlg\crawlerGlg\Data"

def test_method():
    module_count = 1
    modules_dict = {}
    for module in module_list:

        ### zheli
        if module != "image_augmentation-nas_cifar":
            continue
        # try:
        module_dict = {}
        module_path = os.path.join(PATH, module)
        if not os.path.isdir(module_path):
            continue
        file_dir = os.path.join(module_path, "file")
        versions_of_checkpoint = os.listdir(file_dir)
        versions_of_checkpoint.sort()
        print("{}. {} #versions: {}".format(module_count, module, len(versions_of_checkpoint)))
        module_dict["version_num"] = len(versions_of_checkpoint)
        module_count += 1
        versions_dict = {}
        for index in range(len(versions_of_checkpoint)):
            version = versions_of_checkpoint[index]
            module_path = os.path.join(file_dir, version)
            module_hash_value = None
            for fl in os.listdir(module_path):
                if os.path.isdir(os.path.join(module_path, fl)):
                    module_hash_value = fl
                    break
            print("in module: ", module_path)
            tf.reset_default_graph()
            ## remember, the hash value is necessary.
            m = hub.Module(
                ### zheli
                r"https://tfhub.dev/google/{}/1".format(module.replace("-", "/"))
                # os.path.join(module_path, module_hash_value)
            )
            sigs = m.get_signature_names()
            version_api = {}
            for sig in sigs:
                # print("in {}:".format(sig))
                inputs = {
                    k: str(v) #tf.placeholder(v.dtype, v.get_shape().as_list(), k)
                    for k, v in m.get_input_info_dict(sig).items()
                }
                # print(inputs)
                outputs = {
                    k: str(v) #tf.placeholder(v.dtype, v.get_shape().as_list(), k)
                    for k, v in m.get_output_info_dict(sig).items()
                }
                # print(outputs)
                version_api[sig] = {
                    "inputs": inputs,
                    "outputs": outputs
                }
            versions_dict[version] = version_api
            # break
        module_dict["versions"] = versions_dict
        modules_dict[module] = module_dict
        # break
        # except:
        print(f"{module} failed.")

    with open("module_api.json", "w") as ma:
        json.dump(modules_dict, ma, indent=4, sort_keys= True)
    # print(json.dumps(modules_dict, indent=4, sort_keys= True))

test_method()