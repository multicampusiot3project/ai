from django.shortcuts import render

import json
import logging
import os
import cv2
import numpy as np
import torch
from PIL import Image
from torchvision import transforms
from torchvision import models
import torch.nn as nn





CATEGORY = {'dessert': 14}
IMAGE_LABEL = {'input': '', 'output': ''}
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

test_image = '/home/lab20/image/product_image/' + '35102_00_m_1.jpg'
local_image = 'C:\\coding_test\\project\\ai\\imageTest01\\mart_image\\35188_00_m_17.jpg'

#--------- dessert label list ------------
labels = ['25222_대만)망고케익184g', '25228_대만)파인애플케익184G', '35211_매일유업)데르뜨130G', '35584_매일데르뜨파인애플90G',
                          '35585_매일데르뜨감귤90G', '45030_돌황도666G', '45657_씨제이)쁘티첼(요거젤리복숭아)', '45658_씨제이)쁘티첼(요거젤리밀감)',
                          '45659_씨제이)쁘티첼(요거젤리딸기)', '45660_씨제이)쁘티첼(요거젤리화이트코코)', '45661_씨제이)쁘티첼(요거젤리블루베리)',
                          '55034_돌트로피칼666G', '55701_쁘띠첼요거젤리밀감', '55702_쁘띠첼요거젤리복숭아']
labels = {string: i for i, string in enumerate(labels)}
label_decoder = {val: key for key, val in labels.items()}
# --------------


class RegNet(torch.nn.Module):
    def __init__(self):
        super(RegNet, self).__init__()
        model = models.regnet_y_16gf(pretrained=True)
        modules = list(model.children())[:-1]
        self.feature_extract = nn.Sequential(*modules)
        self.fc1 = nn.Linear(3024, 1000)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(1000, CATEGORY['dessert'])

    def forward(self, x):
        x = self.feature_extract(x)
        # (batch, 3024, 1, 1)

        #         x = torch.squeeze(x)
        x = torch.flatten(x, 1)

        x = self.relu(self.fc1(x))
        out = self.fc2(x)

        return out

aws_model_path = '/home/lab20/ai/saved_models/RegNet_1e-05_rmsprop_CosineAnnealing_example.pth'
local_model_path = 'C:\\coding_test\\project\\ai\\result\\RegNet_1e-05_rmsprop_CosineAnnealing_example.pth'

model = RegNet().to(device)
model.load_state_dict(torch.load(local_model_path, map_location='cpu'))



def load_image(image_url):
    test_transform = transforms.Compose([transforms.Resize((256, 256)),
                                         transforms.Normalize(mean=(0.744859, 0.735139, 0.711357), std=(0.100712, 0.120692, 0.167998))])

    image = cv2.imread(image_url).astype(np.float32)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) / 255.0

    image = test_transform(torch.from_numpy(image.transpose(2, 0, 1)))

    return image


def predict(images, device):

    model.eval()
    with torch.no_grad():
        image = torch.as_tensor(images, device=device, dtype=torch.float32)
        preds = model(image)
        preds = torch.softmax(preds, dim=1)
        preds = preds.cpu().numpy()

    return np.array(preds.tolist())


def index(request):
    image_uri = None
    prediction = None

    # if request.method == 'POST':
    image = load_image(local_image)
    image = image.unsqueeze(dim=0)
    # get predicted label

    prediction = predict(image, device)
    prediction = prediction.argmax(axis=1)
    prediction = prediction.tolist()
    prediction = label_decoder[prediction[0]]

    # except RuntimeError as re:
    #     print(re)
        # predicted_label = "Prediction Error"

    # else:
    #     print('error')

    context = {
        'image_uri': local_image,
        'predicted_label': prediction[:5],
    }
    return render(request, 'image_classification/index.html', context)
