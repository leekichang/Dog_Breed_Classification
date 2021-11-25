# %%
import os

DATASET_DIR = './data/'


# %%
os.chdir(DATASET_DIR+"Images")
for (root, directories, files) in os.walk('./'):
    for d in directories:
        d_path = os.path.join(root, d)
        n_path = './'+d_path.split('-')[1]
        os.rename(d_path, n_path)
        print(n_path)

os.chdir("../Annotation/")
for (root, directories, files) in os.walk('./'):
    for d in directories:
        d_path = os.path.join(root, d)
        n_path = './'+d_path.split('-')[1]
        os.rename(d_path, n_path)
        print(n_path)    
# %%
os.chdir("../")

# %%
for (root, directories, files) in os.walk('./Images/'):
    for d in directories:
        d_path = os.path.join(root, d)
        os.mkdir('./test/'+d_path.split('Images/')[1])


# %%
import random as rd
import shutil
rd.seed(100)

for (root, directories, files) in os.walk('./Images/'):
    for d in directories:
        d_path = os.path.join(root, d)
        for (root_, directories_, files_) in os.walk(d_path):
            test_samples = rd.sample(files_, int(len(files_)*0.2))
            for sample in test_samples:
                new_path = shutil.move(f"{d_path}/{sample}", './test/'+d)    
                
            
# %%
os.rename('./Images/', './train')
