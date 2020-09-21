import os, shutil
FILE_DIR = r"J:\ModelStoreData\PyTorchHub\2019-07-30\files"
file_dir = FILE_DIR
for module in os.listdir(file_dir):
    module_dir = os.path.join(file_dir, module)
    # print(module_dir)
    for file in os.listdir(module_dir):
        if file != "webpage.html":
            file_path = os.path.join(module_dir, file)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
            else:
                os.remove(file_path)
            # print(os.path.join(module_dir, file))
print("finished. ")