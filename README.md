# 🖥 AI Team

- [김인후](https://github.com/InhuKim)
- [서지연](https://github.com/Yeony54)
- [심혜주](https://github.com/hjst0223)
- [정민수](https://github.com/yourms)

## 🛒 시각 장애인 마트 쇼핑 서비스

### **✔ 목적**

- 시각 장애인의 쇼핑 편의 향상

### **📢 방향**

- 상품 이미지를 학습하여 상품 인식, 상품 세부 내용 안내
- 장애물을 인식하여 사람일 경우, "사람입니다"를 리턴
- 마트 상품코너 데이터를 토대로 상품 코너 경로 안내

### **🕹 수행 방법▪도구**

- YOLO-v5를 사용한 Object Detecting (객체 탐지)
- Server : AWS ,S3
- IDE : Jupyter Notebook, Google Colab
- Tool : Python, Django
- library : pytorch, opencv, sklearn, matplotlib, numpy, pandas

### **⭐ 필수 기능**

- 상품 촬영 시 이미지 인식 (마트 홈페이지 크롤링 데이터로부터 검색 후 가격 정보 안내 & 유사품과 가격 비교)
- 거리센서로 인식한 장애물을 카메라로 찍어 사람인지 판별
- 마트 내 위치 정보를 통해 경로 안내(카트에 담긴 상품들의 특성에 따른 최적 쇼핑 경로 안내)

### **🔨포함기술**

- 장애물 인식 : raspberry pi 에서 predict 진행
    - YOLO 모델을 사용하여 사람을 인식
    - tensorflow Lite, Yolo Lite 사용하여 라즈베리파이에 올릴 수 있는 경량화된 모델로 제작
- 상품 분류 : Web/서버 에서 predict 진행, pytorch
    - 상품의 카테고리에 따라서 상품 분류 모델 제작(가전, 식품, 생활용품과 같은 다양한 항목)
    - pre-trained model(ResNet, RegNet, EfficientNet, Inception)을 사용해서 fine-tuning하여 최적화
    - 카메라로 찍은 이미지와 해당 위치 정보를 같이 받아서 위치정보에 맞는 상품 분류 모델을 사용

### 📚 데이터

- [딥러닝 기반 다중 CCTV 영상](https://drive.google.com/drive/folders/1el9kK4wgaiMzEMlfzqeQx6acoq703diP)
- [Real-Time Object Detection on COCO](https://paperswithcode.com/sota/real-time-object-detection-on-coco)
- [유사 이미지 찾기](https://velog.io/@chacha/Kaze-Keypoint-Matching-%EC%9C%A0%EC%82%AC-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EC%B0%BE%EA%B8%B0)
- [AIHub 롯데정보통신 상품 이미지 소개](https://aihub.or.kr/aidata/34145)

### 🔍 사례

- [[서비스구현] 시각장애인을 위한 편의점 음료 서비스](https://github.com/se-ize/BeYerage)
- [[서비스(앱)] 설리번+ : 스마트폰 카메라를 통해 인식한 정보를 알려주는 서비스](https://www.mysullivan.org/)
- [[서비스(API)] LG CNS 상품검색 API 서비스](https://www.notion.so/ai.lgcns.com)
- [[논문] 딥러닝 객체 탐지 기술을 사용한 스마트 쇼핑카트의 구현](https://www.koreascience.or.kr/article/JAKO202021853968918.pdf)
- [[뉴스기사] NEC의 상품인식 개발](http://www.aitimes.kr/news/articleView.html?idxno=11439) : 딥러닝 + 특징점 융합
- [[논문, 코드] 로고인식 논문, 소스코드](https://m.facebook.com/groups/TensorFlowKR/permalink/501214233552973/)
- [[서비스구현] 와들프로젝트:시각장애인을 위해 OCR을 사용하여 온라인 쇼핑 페이지를 읽어주는 서비스 (온라인)](https://www.chosun.com/national/national_general/2021/06/15/B2NNB3S35NFHTEHSRJHUUZIICM/)

### Baseline Model

- 성능 비교의 기준이 되는 모델

### 아키텍쳐

![product_classification](https://user-images.githubusercontent.com/96727006/172310429-45af1eb1-be1f-4696-9ef4-98138a3fbada.jpg)

![classification_training_process](https://user-images.githubusercontent.com/96727006/172310480-8be0d009-0453-46ff-a94f-04506564fbc8.jpg)

[테스트 케이스](https://www.notion.so/6d0879ae37bc4ed487a3b0f3708ac9eb)

[기능 구현](https://www.notion.so/7451255c637643e899b9ef84a8a99cac)

# 🛸기능 구현

## ~~0. 사람 Detecting, Tracking~~

- 시각장애인의 위치를 Detecting, Tracking 하여 쇼핑 경로 안내
- 마트에 설치된 카메라로 사용자를 인식, 추적하여 사용자의 위치 정보 생성

> **멘토님 피드백(1주차)**
> 
- 천장에 설치된 CCTV 형식의 카메라로 사람을 Detecting, Tracking은 가능하지만, 위치를 뽑아내는것이 쉽지 않다.
- 경로안내를 IoT로 구현하기로 결정
    - IoT : 위치를 알아낼 수 있는 센서를 사용해서 사용자의 위치 추출
    - AI : 뽑아낸 사용자의 위치데이터를 사용하여 마트 안내

## 1. 장애물 인식

YoloV5 : 실시간 객체 인식 시스템, 기본적으로 80개의 이미지를 구분할 수 있음

라즈베리파이 위에서 사용하기 위해 사이즈가 작은 YOLOv5s를 사용

![image](https://user-images.githubusercontent.com/52309288/175549627-904aa339-a826-47e2-9240-e61d67a32684.png)

> **프로세스**
> 
1. 장애물을 거리센서로 인식, 카메라로 촬영
2. 촬영된 사진을 인식, 사람인지 물체인지 판별
3. 사람일 경우, “사람입니다”를 출력

> **기능 구현, 테스트**
> 
- Yolo 테스트
    - cv2를 사용해 Real Time Detection
    - Model : yolov5, yolov5s
    - Tool : labelimg 각 객체들을 직접 라벨링
    - labeling된 파일을 실행시켜 트레이닝
        
        **`!**python train.py --img 320 --batch 16 --epochs 20 --data dataset.yml --weights yolov5s.pt --workers 2`
        
    - 트레이닝 결과
        
        ![image](https://user-images.githubusercontent.com/52309288/175549707-6db7fbd4-718f-4f6b-9424-02cc2c9735a9.png)
        
- mqtt 연결 테스트
    - 라즈베리파이와 AI서버 통신 연결
- mqtt를 사용하여 Yolo 테스트
    
    ![image](https://user-images.githubusercontent.com/52309288/175549754-fba8bb9f-0045-47e2-8929-46c6c191e801.png)
    

## 2. 상품 분류

> **프로세스**
> 
1. 앱 카메라로 상품 촬영
2. 서버로 이미지와 현재 사용자의 위치를 전송
3. 위치에 해당하는 상품 카테고리의 분류기 호출
4. 분류기 결과 예측값 전달

> **데이터**
> 
- [AIHub 롯데정보통신 상품 이미지](https://aihub.or.kr/aidata/34145)
    - 총 10,280 개의 데이터, 15개의 카테고리로 구성
    - 카테고리 : 과자, 디저트, 면류, 상온 HMR, 생활용품, 소스, 유제품, 음료, 의약외품, 이/미용, 주류, 커피차, 통조림/안주, 홈클린
    - 단수 상품 이미지 72만장, 복수 상품 이미지 72만장 총 144만장 제공
- 빅데이터 수집, 데이터 정제
    
    
    | 과자 | 디저트 | 면류 | 미분류 | 상온 HMR | 생활용품 | 의약외품 | 이/미용 |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | 529 | 14 | 133 | 1 | 342 | 137 | 42 | 197 |
    
    | 소스 | 유제품 | 음료 | 커피차 | 주류 | 통조림/안주 | 홈클린 |
    | --- | --- | --- | --- | --- | --- | --- |
    | 363 | 108 | 450 | 133 | 34 | 131 | 126 |
- 데이터가 너무 많아서 학습이 어려워 데이터를 줄여서 하기로 함
    - 40개 클래스 한 에폭당 4분

> **기능구현, 테스트**
> 
- 상품 인식 모델 생성
    - pytorch
    - Model : ResNet50, EfficientNetb4, RegNet
    - Learning Rate : 1e-3, 1e-4. 1e-5
    - Optimizer : adam, lamb, rmsprop, nadam
    - Normalize : train, valid 데이터 각 RGB 픽셀의 평균(mean), 표준편차(std)를 계산하여 Normalize 진행
    - Augmentation : albumentations의 무작위 Crop, 밝기 조정, 회전 기능을 사용하여 data augmentation 진행
    - Scheduler : pytorch의 CosineAnnealingLR를 사용하여 epoch에 따라 학습률 조정(최소 학습률과 반주기 지정)
- 모델 학습
    - 각 Model, Optimizer, Learning Rate 를 사용해 test data set(디저트 14종)을 학습
    - 학습한 결과, (Regnet, 1e-5, rmsprop) 학습에서 accuracy가 0.935 로 가장 높았다.
    
    ![image](https://user-images.githubusercontent.com/52309288/175549827-a92316e1-5953-4476-8394-f8d4530e294f.png)
    
    - 이 이외에도 Regnet에서 가장 좋은 성능을 보여주었다.
    - lamb accuracy가 떨어짐 → 학습을 할수록 엉뚱하게 분류
    - rmsprop → 학습을 촘촘히 할수록 제대로 분류
- 상품 카테고리 선정
    - 매대 4개
    - 디저트,  의약외품, 홈클린, 상온HMR
- 최종 모델 학습
    - ~ing
- 한계
    - 상품의 이미지가 변경되면, 다시 학습을 해야한다
    - 같은상품 다른 크기의 상품을 구별하기 어렵다
- 해결방법
    - OCR, 로고인식 등의 기술을 추가
    

## 3. 경로 안내

> **1주차 피드백**
> 
- 매장 내 코스를 제작하여 위치 정보를 입력하여 프로토 타입 제작

> **프로세스**
> 

최단경로탐색 알고리즘, 비콘과 연동하여 경로를 안내

1. 서버로부터 사용자의 위치 가져옴
2. 현재 사용자의 위치에서 목표지점까지의 최단경로 생성
3. 목적지 까지 가는 경로 안내

> **기능구현, 테스트**
> 
- 코드
    - 사용자가 상품 리스트를 입력
    - 카트의 최적화 경로를 표시
    - 상품마대는 주황, 거쳐야할곳은 연두, 상품Stand는 자주색으로 표시
    - 아래 숫자에 마우스를 올리면 경로표시
    - 한칸씩, 한칸만 으로 예상 경로 표시
- 구동 화면
    
    <img src="https://user-images.githubusercontent.com/52309288/175549914-ac1b13a8-9f30-4f4d-9e78-26e1bded3012.png" width="350" height="350">
    
- 동영상 링크
    
    [Video](https://youtu.be/HMvhI344gSo)
