
import json
import logging
import os
import torch
from PIL import Image
from torchvision import transforms
from torchvision import models
import torch.nn as nn

from cgi import test
import threading
import paho.mqtt.client as mqtt
from threading import Thread, Event
import paho.mqtt.publish as publisher
import time

count =0
img_count = 0 


import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import torchvision.transforms as transforms
import os
import shutil
from PIL import Image
from datetime import datetime

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def predict_object():
    start = time.time()  # 시작 시간 저장
    global count
    count += 1
    now = datetime.now()
#     img = PIL.Image.open('C:/Users/yourm/Desktop/yunghab3/yolo_test/mart_image/{}.jpg'.format(count))
    img = Image.open('/home/lab19/image/result/test{}.jpg'.format(count))
    #img = Image.open('/home/lab19/image/person.jpg')
    #img.show()
    
    start3 = time.time()  # 시작 시간 저장
    results = model(img)
    print("time model :", time.time() - start3)  # 현재시각 - 시작시간 = 실행 시간

    
    #이미지를 보여주기 위한 save  나중에 지워도됨
    #results.save(save_dir='C:/Users/yourm/Desktop/yunghab3/yolo_test/runs/detect/exp_1')
    
    image_df = results.pandas().xyxy[0]
    person_img = image_df[image_df['name'] == 'person']
    
    # Person 이 1명이라도 있으면 실행
    if(person_img.shape[0] > 0):
        for idx in range(0, person_img.shape[0], 1):
            # 사람의 크기가 가로, 세로 반이 넘으면 사람으로 판단
            if(((person_img.iloc[idx]['xmax'] - person_img.iloc[idx]['xmin']) > (img.width/2)) and 
               ((person_img.iloc[idx]['ymax'] - person_img.iloc[idx]['ymin']) > (img.height/2))): 
                start4 = time.time()  # 시작 시간 저장
                results.save(save_dir='/home/lab19/image/result/detection')
                print("time save :", time.time() - start4)  # 현재시각 - 시작시간 = 실행 시간
                print("4")
                person = "person"
                print("time predict_object :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
                return person
            else: 
                person = "none"
                print("time predict_object :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
                return person

# 통신 부분
class MqttWorker:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.exit_event = Event()

    def signal_handler(self, signum, frame):
        print("signal_handler===================================")
        self.exit_event.set()  # 이벤트객체가 갖고 있는 플래그 변수가 True로 셋팅
        self.led.clean()
        # 현재 이벤트 발생을 체크하고 다른 작업을 수행하기 위한 코드 - 다른 메소드에서 처리
        if self.exit_event.is_set():
            print(
                "이벤트객체의 플래그변수가 Ture로 바뀜 - 이벤트가 발생하면 어떤 작업을 실행하기 위해서(다른 메소드 내부에서 반복문 빠져나오기~....)")
            exit(0)

    def mymqtt_connect(self):  # 사용자정의 함수 - mqtt서버연결과 쓰레드생성 및 시작을 사용자정의 함수로 정의
        try:
            self.client.connect("13.52.187.248", 1883, 60)
            mythreadobj = Thread(target=self.client.loop_forever)
            mythreadobj.start()
            
        except KeyboardInterrupt:
            pass
        finally:
            print("종료")

    def on_connect(self, client, userdata, flags, rc):  # broker접속에 성공하면 자동으로 호출되는 callback함수
        if rc == 0:  # 연결이 성공하면 구독신청
            client.subscribe("mydata/file")
            client.subscribe("android/#")
            client.subscribe("iot/picamera")
        else:
            print("연결실패.....")

    # 라즈베리파이가 메시지를 받으면 호출되는 함수이므로 받은 메시지에 대한 처리를 구현
    def on_message(self, client, userdata, message):
        try:
            start2 = time.time()  # 시작 시간 저장
            myval2 = message.topic.split("/")
            print("myval2 : ",myval2)
            if myval2[1] == "object":
                print(message.payload)
            if myval2[1] == "picamera":
                result_object = predict_object()
                print("result_object : ", result_object)
            publisher.single("android/productAI", result_object, hostname="13.52.187.248")
            print("time on_message :", time.time() - start2)  # 현재시각 - 시작시간 = 실행 시간
            
        except:
            pass
        finally:
            pass


# 테스트 작업을 위한 클래스
if __name__ == '__main__':
    try:
        mqtt = MqttWorker()
        mqtt.mymqtt_connect()  # callback 함수가 아니므로 인스턴스 변수를 이용해서 호출해야 한다.
        for i in range(10):
            print(i)

    except KeyboardInterrupt:
        pass

    finally:

        print("종료")
