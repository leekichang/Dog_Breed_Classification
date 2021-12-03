import torch
import torchvision.models as models

from model_config import get_model_names
from model_config import get_model

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

model_names = get_model_names()

for model_name in model_names:
    model = get_model(model_name)
    print(model_name, end='')
    print(count_parameters(model))