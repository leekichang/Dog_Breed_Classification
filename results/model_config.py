import os
import torchvision.models as models

def get_model(model_name):
    if model_name == 'vgg16':
        return models.vgg16(pretrained=False)
    
    elif model_name == 'vgg19':
        return models.vgg19(pretrained=False)
    
    elif model_name == 'ResNet34':
        return models.resnet34(pretrained=False)
    
    elif model_name == 'ResNet50':
        return models.resnet50(pretrained=False)
    
    elif model_name == 'ResNet101':
        return models.resnet101(pretrained=False)
    
    elif model_name == 'ResNet152':
        return models.resnet152(pretrained=False)
    
    elif model_name == 'DenseNet':
        return models.densenet161(pretrained=False)
    
    elif model_name == 'EfficientNet_b0':
        return models.efficientnet_b0(pretrained=False)
    
    elif model_name == 'EfficientNet_b6':
        return models.efficientnet_b6(pretrained=False)
    
    elif model_name == 'EfficientNet_b7':
        return models.efficientnet_b7(pretrained=False)
    
    elif model_name == 'mobileNet_large':
        return models.mobilenet_v3_large(pretrained=False)
    
    elif model_name == 'mobileNet_small':
        return models.mobilenet_v3_small(pretrained=False)
    
    elif model_name == 'RegNet_x_400mf':
        return models.regnet_x_400mf(pretrained=False)
    
    elif model_name == 'RegNet_y_32gf':
        return models.regnet_y_32gf(pretrained=False)



def get_model_names():
    files = [file for file in os.listdir('./') if file.endswith('.txt')]
    model_names = []

    for file in files:
        model_names.append(file.split('.')[0])
    return model_names

if __name__ == "main":
    print()