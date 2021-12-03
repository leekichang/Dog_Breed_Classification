import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import os

TNR = fm.FontProperties(fname='../font/times.ttf')

files = [file for file in os.listdir('./') if file.endswith('.txt')]
mpl.rcParams['axes.unicode_minus'] = False

# for file in files:
#     model_name = file.split('.')[0]
#     f = open(f'./{file}', 'r')
#     data = f.read().strip()
#     epoch = int(data.split(')')[0].split('/')[1])
#     train_loss = []
#     val_loss = []
#     acc = []
#     print(model_name)
#     for s in data.split('%')[:-1]:
#         s_ = s.split('|')
#         train_loss.append(float(s_[0].split(':')[1]))
#         val_loss.append(float(s_[1].split(':')[1]))
#         acc.append(float(s_[2].split(':')[1]))
                        
#     

#     plt.rcParams["figure.figsize"] = (20, 10)
#     plt.rcParams["axes.titlesize"] = 20
#     plt.figure()
#     plt.title(f'Training and Validation Loss({model_name})', fontproperties = TNR, fontsize = 25)
#     plt.plot(range(1,epoch+1), train_loss, label="Training Loss")
#     plt.plot(range(1,epoch+1), val_loss, label="Validation Loss")
#     plt.xlabel('Epoch', fontproperties = TNR, fontsize=23)
#     plt.ylabel('Loss', fontproperties = TNR, fontsize=23)
#     plt.xticks(fontproperties = TNR, fontsize=23)
#     plt.yticks(fontproperties = TNR, fontsize=23)
#     plt.xlim((1,epoch+1))
#     plt.legend()
#     plt.tight_layout()
#     plt.savefig(f'./loss/{model_name}_loss.png')
#     plt.close()
    
#     plt.rcParams["figure.figsize"] = (20, 10)
#     plt.rcParams["axes.titlesize"] = 20
#     plt.figure()
#     plt.title(f'Accuracy({model_name})', fontproperties = TNR, fontsize = 25)
#     plt.plot(range(1,epoch+1), acc, label="Validation Accuracy")
#     plt.xlabel('Epoch', fontproperties = TNR, fontsize=23)
#     plt.ylabel('Accuracy', fontproperties = TNR, fontsize=23)
#     plt.xticks(fontproperties = TNR, fontsize=23)
#     plt.yticks(fontproperties = TNR, fontsize=23)
#     plt.xlim((1,epoch+1))
#     plt.legend()
#     plt.tight_layout()
#     plt.savefig(f'./acc/{model_name}_acc.png')
#     plt.close()
    

# ALL MODELS IN ONE FIGURE
# train_loss = [[] for idx in range(len(files))]
# val_loss = [[] for idx in range(len(files))]
# acc = [[] for idx in range(len(files))]
# model_name = []
# for idx, file in enumerate(files):
#     model_name.append(file.split('.')[0])
#     f = open(f'./{file}', 'r')
#     data = f.read().strip()
#     epoch = int(data.split(')')[0].split('/')[1])
#     for s in data.split('%')[:-1]:
#         s_ = s.split('|')
#         train_loss[idx].append(float(s_[0].split(':')[1]))
#         val_loss[idx].append(float(s_[1].split(':')[1]))
#         acc[idx].append(float(s_[2].split(':')[1]))
                        
# mpl.rcParams['axes.unicode_minus'] = False

# plt.rcParams["figure.figsize"] = (20, 10)
# plt.rcParams["axes.titlesize"] = 20
# plt.figure()
# for idx in range(len(files)):
#     plt.plot(range(1,11), train_loss[idx][:10], label=f"{model_name[idx]} train")
#     plt.plot(range(1,11), val_loss[idx][:10], label=f"{model_name[idx]} val")

# plt.title(f'Train and Validation Loss(All models)', fontproperties = TNR, fontsize = 25)
# plt.xlabel('Epoch', fontproperties = TNR, fontsize=23)
# plt.ylabel('Loss', fontproperties = TNR, fontsize=23)
# plt.xticks(fontproperties = TNR, fontsize=23)
# plt.yticks(fontproperties = TNR, fontsize=23)
# plt.xlim((1,10))
# plt.legend(loc = 'upper right')
# plt.tight_layout()
# plt.savefig(f'./loss/All_model_loss.png')
# plt.close()

# for idx in range(len(files)):
#     plt.plot(range(1,11), train_loss[idx][:10], label=f"{model_name[idx]}")

# plt.title(f'Train Loss(All models)', fontproperties = TNR, fontsize = 25)
# plt.xlabel('Epoch', fontproperties = TNR, fontsize=23)
# plt.ylabel('Loss', fontproperties = TNR, fontsize=23)
# plt.xticks(fontproperties = TNR, fontsize=23)
# plt.yticks(fontproperties = TNR, fontsize=23)
# plt.xlim((1,10))
# plt.legend()
# plt.tight_layout()
# plt.savefig(f'./loss/All_model_train_loss.png')
# plt.close()


# for idx in range(len(files)):
#     plt.plot(range(1,11), val_loss[idx][:10], label=f"{model_name[idx]}")

# plt.title(f'Validation Loss(All models)', fontproperties = TNR, fontsize = 25)
# plt.xlabel('Epoch', fontproperties = TNR, fontsize=23)
# plt.ylabel('Loss', fontproperties = TNR, fontsize=23)
# plt.xticks(fontproperties = TNR, fontsize=23)
# plt.yticks(fontproperties = TNR, fontsize=23)
# plt.xlim((1,10))
# plt.legend()
# plt.tight_layout()
# plt.savefig(f'./loss/All_model_val_loss.png')
# plt.close()

# plt.figure()
# for idx in range(len(files)):
#     plt.plot(range(1,11), acc[idx][:10], label=f"{model_name[idx]}")
# plt.title(f'Accuracy(All models)', fontproperties = TNR, fontsize = 25)
# plt.xlabel('Epoch', fontproperties = TNR, fontsize=23)
# plt.ylabel('Accuracy', fontproperties = TNR, fontsize=23)
# plt.xticks(fontproperties = TNR, fontsize=23)
# plt.yticks(fontproperties = TNR, fontsize=23)
# plt.xlim((1,10))
# plt.legend()
# plt.tight_layout()
# plt.savefig(f'./acc/All_model_acc.png')
# plt.close()


# Put all of them in subfigures
# plt.subplot(7,2,14)
#plt.figure(constrained_layout = True)
plt.rcParams["figure.figsize"] = (10, 15)
plt.rcParams["axes.titlesize"] = 10

# for idx, file in enumerate(files):
#     model_name = file.split('.')[0]
#     f = open(f'./{file}', 'r')
#     data = f.read().strip()
#     epoch = int(data.split(')')[0].split('/')[1])
#     train_loss = []
#     val_loss = []
#     acc = []
#     print(model_name)
#     for s in data.split('%')[:-1]:
#         s_ = s.split('|')
#         train_loss.append(float(s_[0].split(':')[1]))
#         val_loss.append(float(s_[1].split(':')[1]))
#         acc.append(float(s_[2].split(':')[1]))

#     print( 7*(idx//7) + idx%7 + 1)
#     plt.subplot(7,2, 7*(idx//7) + idx%7 + 1)
#     plt.plot(range(1,epoch+1), train_loss, label="Training Loss")
#     plt.plot(range(1,epoch+1), val_loss, label="Validation Loss")
#     plt.title(f'Training and Validation Loss({model_name})', fontproperties = TNR, fontsize = 12.5)
#     plt.xlabel('Epoch', fontproperties = TNR, fontsize=10)
#     plt.ylabel('Loss', fontproperties = TNR, fontsize=10)
#     plt.xticks(fontproperties = TNR)
#     plt.yticks(fontproperties = TNR)
#     plt.xlim((1,epoch))
#     plt.legend(loc='upper right', fontsize=5)
#     plt.tight_layout()
#plt.show()
for idx, file in enumerate(files):
    model_name = file.split('.')[0]
    f = open(f'./{file}', 'r')
    data = f.read().strip()
    epoch = int(data.split(')')[0].split('/')[1])
    train_loss = []
    val_loss = []
    acc = []
    print(model_name)
    for s in data.split('%')[:-1]:
        s_ = s.split('|')
        train_loss.append(float(s_[0].split(':')[1]))
        val_loss.append(float(s_[1].split(':')[1]))
        acc.append(float(s_[2].split(':')[1]))

    print( 7*(idx//7) + idx%7 + 1)
    plt.subplot(7,2, 7*(idx//7) + idx%7 + 1)
    plt.plot(range(1,epoch+1), acc, label="Training Loss")
    plt.title(f'Accuracy({model_name})', fontproperties = TNR, fontsize = 12.5)
    plt.xlabel('Epoch', fontproperties = TNR, fontsize=10)
    plt.ylabel('Accuracy', fontproperties = TNR, fontsize=10)
    plt.xticks(fontproperties = TNR)
    plt.yticks(fontproperties = TNR)
    plt.xlim((1,epoch))
    plt.legend(loc='lower right', fontsize=5)
    plt.tight_layout()
plt.savefig(f'./asdasdasd.png')