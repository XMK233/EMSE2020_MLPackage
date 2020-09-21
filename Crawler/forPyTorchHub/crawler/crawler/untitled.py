import torch, os, shutil, time

FROM_DIR = r"C:\Users\xmk233\.cache\torch"
FILE_PATH = r"J:\ModelStoreData\PyTorchHub\2020-01-07\files"
def test():
    ## 
    model_name = "ProxylessNAS"
    ## 
    model1 = torch.hub.load('mit-han-lab/ProxylessNAS', "proxyless_cpu", pretrained=True)
    model2 = torch.hub.load('mit-han-lab/ProxylessNAS', "proxyless_gpu", pretrained=True)
    model3 = torch.hub.load('mit-han-lab/ProxylessNAS', "proxyless_mobile", pretrained=True)
    model4 = torch.hub.load('mit-han-lab/ProxylessNAS', "proxyless_mobile_14", pretrained=True)
    model1.eval()
    model2.eval()
    model3.eval()
    model4.eval()
    ######
    shutil.move(FROM_DIR, os.path.join(FILE_PATH, model_name, "torch"))
    return

test()