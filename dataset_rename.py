# %%
import os

DATASET_DIR = './data/'


# %%
os.chdir(DATASET_DIR+"images")
for (root, directories, files) in os.walk('./'):
    for d in directories:
        d_path = os.path.join(root, d)
        n_path = './'+d_path.split('-')[1]
        os.rename(d_path, n_path)
        print(n_path)

os.chdir("../annotation/")
for (root, directories, files) in os.walk('./'):
    for d in directories:
        d_path = os.path.join(root, d)
        n_path = './'+d_path.split('-')[1]
        os.rename(d_path, n_path)
        print(n_path)        


