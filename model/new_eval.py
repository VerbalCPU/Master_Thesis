import torch
import torch.backends.cudnn as dudnn
import torch.nn.parallel
import torch.optim
import torch.utils.data
import torchvision.transforms as transforms
import numpy as np
from models import resnet101_CHR
from ray import XrayClassification
from util import AveragePrecisionMeter, Warp
from PIL import Image
from torch.autograd import Variable
import glob
print("imports ok")

#load model
path_best_model = "/home/emmachal/manos_project/CHR/CHR/CHR/models-/model_best.pth.tar"
print("path ok")


num_classes = 5
model = resnet101_CHR(num_classes, pretrained=True)
model.cuda()
checkpoint = torch.load(path_best_model)
model.load_state_dict(checkpoint['state_dict'])
print("model loaded")


model.eval()

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

'''
path = r"/media/Data_RAID/wamus/SIXray/JPEGImage/"

new_pos_list = ["P01769","P01772","P01774","P01778","P01779","P01786","P01793","P01797","P01809","P01811","P01815",
		"P01817","P01855","P01871","P01891","P01895","P01896","P01906","P01907","P01913","P01917","P01919",
		"P01920"]

print("ok until here")
for i in range(len(new_pos_list)):
    for filename in glob.glob(path+new_pos_list[i]+'.jpg'):
        im = Image.open(filename)
        print(filename)
        input_tensor = preprocess(im)
        input_batch = input_tensor.unsqueeze(0)
        output = model(Variable(input_batch).float().cuda())
        probabilities = torch.nn.functional.softmax(output[0],dim=1)
        print(probabilities)
'''
print("ok here")
path = r"/home/emmachal/manos_project/energies/dataset/high/clu/"

for filename in glob.glob(path+'*.jpg'):
    im = Image.open(filename)
    print(filename)
    input_tensor = preprocess(im)
    input_batch = input_tensor.unsqueeze(0)
    output = model(Variable(input_batch).float().cuda())
    probabilities = torch.nn.functional.softmax(output[0],dim=1)
    print(probabilities)

print("done")
