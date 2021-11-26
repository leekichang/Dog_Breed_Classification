import torchvision.models as models
import torch.nn as nn

def load_model(model_name = 'denseNet161', num_of_classes = 120, pretraining = True):
    model = models.densenet161(pretrained = pretraining)
    if model_name == "densenet161":
        model = models.densenet161(pretrained = pretraining)
        for param in model.features.parameters():
            param.requires_grad = False
        num_of_inputs = model.classifier.in_features
        last_layer = nn.Linear(num_of_inputs, num_of_classes)
        model.classifier = last_layer

    elif model_name == "mobilenet_v3_large":
        model = models.mobilenet_v3_large(pretrained = pretraining)
        for param in model.features.parameters():
            param.requires_grad = False
        num_of_inputs = model.classifier[0].in_features
        last_layer = nn.Linear(num_of_inputs, num_of_classes)
        model.classifier = last_layer
        
    elif model_name == "mobilenet_v3_small":
        model = models.densenet161(pretrained = pretraining)
        for param in model.features.parameters():
            param.requires_grad = False
        num_of_inputs = model.classifier.in_features
        last_layer = nn.Linear(num_of_inputs, num_of_classes)
        model.classifier = last_layer
        
    elif model_name == "inception":
        model = models.inception_v3(pretrained = pretraining)
        for param in model.parameters():
            param.requires_grad = False
        num_of_inputs = model.fc.in_features
        last_layer = nn.Linear(num_of_inputs, num_of_classes)
        model.classifier = last_layer
        
    elif model_name == "efficientnet_b0":
        model = models.efficientnet_b0(pretrained = pretraining)
        #Try this with torchvision===0.11.1 I've 0.10.0 version for my gpu dependency...
        
    elif model_name == "resnet50":
        model = models.resnet50(pretrained = pretraining)
        for param in model.parameters():
            param.requires_grad = False
        num_of_inputs = model.fc.in_features
        last_layer = nn.Linear(num_of_inputs, num_of_classes)
        model.classifier = last_layer
        
    elif model_name == "resnet101":
        model = models.resnet101(pretrained = pretraining)
        for param in model.parameters():
            param.requires_grad = False
        num_of_inputs = model.fc.in_features
        last_layer = nn.Linear(num_of_inputs, num_of_classes)
        model.classifier = last_layer
        
    elif model_name == "resnet34":
        model = models.resnet34(pretrained = pretraining)
        for param in model.parameters():
            param.requires_grad = False
        num_of_inputs = model.fc.in_features
        last_layer = nn.Linear(num_of_inputs, num_of_classes)
        model.classifier = last_layer
    
    return model
    