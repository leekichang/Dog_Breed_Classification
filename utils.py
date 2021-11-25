import torch
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torchvision.datasets as dset
from sklearn.model_selection import train_test_split

def load_dataset(DATASET_DIR = './data/', image_height = 224, BATCH_SIZE = 256):
    
    train_dir = DATASET_DIR+'train/'
    test_dir = DATASET_DIR+'test/'
    train_transforms = transforms.Compose([transforms.RandomRotation(10),
                                    transforms.RandomHorizontalFlip(),
                                    transforms.RandomResizedCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                        std=[0.229, 0.224, 0.225])])

    test_transforms = transforms.Compose([transforms.RandomResizedCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                        std=[0.229, 0.224, 0.225])])

    TRAIN_SET = dset.ImageFolder(root=train_dir, transform = train_transforms)
    TEST_SET = dset.ImageFolder(root=test_dir, transform = test_transforms)
    
    train_loader = torch.utils.data.DataLoader(TRAIN_SET, batch_size=BATCH_SIZE, shuffle=True, drop_last=True)
    test_loader = torch.utils.data.DataLoader(TEST_SET, batch_size=BATCH_SIZE, shuffle=False, drop_last=False)
    
    return TRAIN_SET, TEST_SET, train_loader, test_loader


import seaborn as sns
import sklearn.metrics as metrics
import numpy as np
import matplotlib.pyplot as plt

def get_metrics(models, pred, anno, num_of_labels=120):
    for model_idx in range(len(models)):
        print(np.shape(pred[model_idx]))
        print(np.shape(anno[model_idx]))
        print(metrics.accuracy_score(anno[model_idx], pred[model_idx]))
        conf_mat = metrics.confusion_matrix(anno[model_idx], pred[model_idx])
        print(conf_mat)
        print(metrics.classification_report(anno[model_idx], pred[model_idx]))

        plt.rcParams["figure.figsize"] = (num_of_labels, num_of_labels)
        sns.heatmap(conf_mat, annot=True, fmt='d', cmap='Blues')
        plt.show()
        conf_mat_sum = np.sum(conf_mat, axis=1)
        conf_mat_sum = np.reshape(conf_mat_sum, (num_of_labels, 1))
        sns.heatmap(conf_mat/conf_mat_sum, annot=True, fmt='.2%', cmap='Blues')