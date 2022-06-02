<<<<<<< HEAD
# mulcam3project_personal
Detecting Product......
=======
# 🖥 AI Team
- [김인후](https://github.com/InhuKim)
- [서지연](https://github.com/Yeony54)
- [심혜주](https://github.com/hjst0223)
- [이지희](https://github.com/2-Jihee)
- [정민수](https://github.com/yourms)
## 🛒 시각 장애인 마트 쇼핑 서비스 
- [프로젝트 상세 보기](https://github.com/multicampusiot3project/info)
### ✔ 목적
- 시각 장애인의 쇼핑 편의 향상
### 📢 방향
- 상품 이미지를 학습하여 상품 인식, 상품 세부 내용 안내
- ~~시각장애인의 위치를 Detecting, Tracking 하여 쇼핑 경로 안내~~
- 마트 상품코너 데이터를 토대로 상품 코너 경로 안내
### 🕹 수행 방법▪도구
- Object Tracking (객체 탐지 및 추적 방법)
  - model : YOLO-v3, Deep Sort (딥러닝 기반 실시간 다중 추적 시스템)
  - 실험 데이터 : MOT16, MOT challenge benchmark (CCTV 영상처럼 구성)
- OCR, Image Detect 둘다 함께 써서 정확도를 높이고자 함
- IDE : Jupyter Notebook
- Tool : Python
- library : pytorch, opencv, sklearn, matplotlib, numpy, pandas
### ⭐ 필수 기능
- 상품명 촬영 시 이미지 인식 (마트 홈페이지 크롤링 데이터로부터 검색 후 가격 정보 안내 & 유사품과 가격 비교)
- 마트에 설치된 카메라로 사용자를 인식, 추적하여 사용자의 위치 정보 생성
- 마트 내 위치 정보를 통해 경로 안내(카트에 담긴 상품들의 특성에 따른 최적 쇼핑 경로 안내)
### 🔨포함기술
- 장애물 인식 : raspberry pi 에서 predict 진행
    - YOLO 모델을 사용하여 사람을 인식
    - tensorflow Lite 사용하여 라즈베리파이에 올릴 수 있는 경량화된 모델로 제작
- 상품 분류 : Web에서 predict 진행, pytorch
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
- [[서비스(앱)] 설리번+ : 스마트폰 카메라를 통해 인식한 정보를 알려주는 서비스 ](https://www.mysullivan.org/)
- [[서비스(API)] LG CNS 상품검색 API 서비스](ai.lgcns.com)
- [[논문] 딥러닝 객체 탐지 기술을 사용한 스마트 쇼핑카트의 구현](https://www.koreascience.or.kr/article/JAKO202021853968918.pdf)
- [[뉴스기사] NEC의 상품인식 개발](http://www.aitimes.kr/news/articleView.html?idxno=11439) : 딥러닝 + 특징점 융합
- [[논문, 코드] 로고인식 논문, 소스코드](https://m.facebook.com/groups/TensorFlowKR/permalink/501214233552973/)
- [[서비스구현] 와들프로젝트:시각장애인을 위해 OCR을 사용하여 온라인 쇼핑 페이지를 읽어주는 서비스 (온라인)](https://www.chosun.com/national/national_general/2021/06/15/B2NNB3S35NFHTEHSRJHUUZIICM/)
>>>>>>> 1101aea33c29badf69ac5e65c9edbf32de73cbcd
