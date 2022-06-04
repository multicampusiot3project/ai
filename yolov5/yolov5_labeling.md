### 라벨링 

![20220604_175906](https://user-images.githubusercontent.com/34851766/171992541-1517e1ad-c8cf-439a-9b53-3e783d92bb23.png)

1. Open Dir - data/images 폴더 선택
2. Change Save Dir - data/labels 폴더 선택(생성)
3. 아래 save 버튼 아래에 Yolo 로 변경
4. File List의 맨 위 이미지 선택

![20220604_181019](https://user-images.githubusercontent.com/34851766/171992706-1416177f-c777-447f-8753-6d3024711234.png)


5. W 키를 누르거나 Create RectBox 키를 누른후 영역지정
6. labelimg에 맞는 class( awake 나 drowsy) 입력후 OK 클릭
7. ctrl + S 키로 저장 후 다음 그림 선택
8. 영역지정 - 저장 계속 반복 다 저장하면 라벨링작업 끝



###  dataset.xml 만들기

![20220604_181757](https://user-images.githubusercontent.com/34851766/171993055-624ad5ac-7c64-435b-bfa9-13343879d86b.png)


1. yolov5 폴더에 dataset.yml or dataset.yaml 생성/수정(visual studio code로 생성)
2. data 폴더밑에 coco128.yaml 파일을 복사 & 붙여넣기하여 수정



#### Colab 에서 training 시킬때 labels, images, dataset.yml 넣어주면 된다.


![20220604_182512](https://user-images.githubusercontent.com/34851766/171993397-cf1a12e6-e7c1-4c2a-9c09-b46747f525c6.png)
![20220604_182518](https://user-images.githubusercontent.com/34851766/171993399-c7fa7227-71f9-435d-8e18-d1b383bfc350.png)

##### training이 끝나면 pt 모델을 다운로드

![20220604_182523](https://user-images.githubusercontent.com/34851766/171993401-24ec188a-e18e-4c86-bb1f-ab8e13b74636.png)
