from settings import FILES_STORE
import os, shutil

def delete_files(suffix):
    for name in os.listdir(FILES_STORE):
        if name == "full":
            continue
        if not os.path.isdir(os.path.join(FILES_STORE, name)):
            continue
        model_dir = os.path.join(FILES_STORE, name)
        for file in os.listdir(model_dir):
            entity_to_remove = os.path.join(model_dir, file, "file")
            if os.path.exists(entity_to_remove):
                shutil.rmtree(os.path.join(model_dir, file, "file"))
            ######
            # if os.path.isfile():
            #     if suffix in file:
            #         os.remove(os.path.join(model_dir, file))
            # else:
            #     pass

delete_files(".ipynb")