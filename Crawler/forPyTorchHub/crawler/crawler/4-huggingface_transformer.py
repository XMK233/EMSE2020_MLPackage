import torch, os, shutil, time

FROM_DIR = r"C:\Users\xmk233\.cache\torch\transformers"
FILE_PATH = r"J:\ModelStoreData\PyTorchHub\2020-01-07\files\PyTorch-Transformers"
def test(model_name):
    time.sleep(1)
    # try:
    ###
    print("Downloading {}...".format(model_name))
    if model_name == "gpt2-large" or model_name == "gpt2-xl": 
        model = torch.hub.load('huggingface/pytorch-transformers', 'model', model_name, from_tf = True)
    else:
        model = torch.hub.load('huggingface/pytorch-transformers', 'model', model_name)
    ######
    shutil.move(FROM_DIR, os.path.join(FILE_PATH, model_name))
    # except:
    #     with open("failed_transformer.txt", "a") as ft:
    #         ft.write("{}\n".format(model_name))
    return

# test('bert-base-cased')
# test('bert-base-german-dbmdz-cased')
# test('bert-base-german-dbmdz-uncased')
# test('bert-base-japanese')
# test('bert-base-japanese-char')
# test('bert-base-japanese-char-whole-word-masking')
# test('bert-base-japanese-whole-word-masking')
# test('bert-base-multilingual-cased')
# test('bert-base-uncased')
# test('bert-large-cased')
# test('bert-large-cased-whole-word-masking')
# test('bert-large-cased-whole-word-masking-finetuned-squad')
# test('bert-large-uncased')
# test('bert-large-uncased-whole-word-masking')
# test('bert-large-uncased-whole-word-masking-finetuned-squad')
# test('distilbert-base-german-cased')
# test('distilbert-base-multilingual-cased')
# test('distilbert-base-uncased')
# test('distilbert-base-uncased-distilled-squad')
# test('gpt2')
# test('gpt2-large')
# test('gpt2-medium')
# test('gpt2-xl')
# test('openai-gpt')
# test('roberta-base')
# test('roberta-base-openai-detector')
# test('roberta-large')
# test('roberta-large-openai-detector')
# test('transfo-xl-wt103')
# test('xlm-clm-ende-1024')
# test('xlm-clm-enfr-1024')
# test('xlm-mlm-ende-1024')
# test('xlm-mlm-enfr-1024')
# test('xlm-mlm-tlm-xnli15-1024')
# test('xlm-mlm-xnli15-1024')
# test('xlnet-base-cased')
# test('xlnet-large-cased')

## the following is the 2020-04-12 newly added ones. 
# test('bert-base-finnish-cased-v1')
# test('bert-base-cased-finetuned-mrpc')
# test('distilbert-base-cased-distilled-squad')
# test('roberta-large-mnli')
# test('xlm-mlm-enro-1024')
# test('distilgpt2')
# test('bert-base-finnish-uncased-v1')
# test('xlm-mlm-en-2048')
# test('bert-base-multilingual-uncased')
# test('bert-base-chinese')
# test('xlm-mlm-100-1280')
# test('distilroberta-base')
# test('distilbert-base-cased')
test('xlm-mlm-17-1280')
test('bert-base-dutch-cased')
test('bert-base-german-cased')