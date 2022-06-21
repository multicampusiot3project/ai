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
import threading
import paho.mqtt.client as mqtt
from threading import Thread, Event
import paho.mqtt.publish as publisher




CATEGORY = {'dessert': 14}
IMAGE_URL = {'input': '', 'output': ''}
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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

model = RegNet().to(device)
model.load_state_dict(torch.load('./../../saved_models/RegNet_1e-05_rmsprop_CosineAnnealing_example.pth'))



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

    return np.array(preds)


def index(request):
    image_uri = None
    predicted_label = None

    if request.method == 'POST':
        image = load_image('/home/lab18/imageTest01/mart_image/' + '1.jpg')
            # get predicted label
        try:
            predicted_label = predict(image)
        except RuntimeError as re:
            print(re)
            # predicted_label = "Prediction Error"

    else:
        print('error')

    context = {
        'form': form,
        'image_uri': image_uri,
        'predicted_label': predicted_label,
    }
    return render(request, 'image_classification/index.html', context)
