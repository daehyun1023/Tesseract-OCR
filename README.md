## 1. 프로젝트 목표
- 행정 문서로부터 ***한글 텍스트***를 추출하는 ***OCR Performance 향상***  
- 오픈소스인 Tesseract 4.0버전으로 광학문자인식기 개발  
## 2. 프로젝트 과정
![pipeline](https://user-images.githubusercontent.com/65157567/96362520-e1f2f880-1168-11eb-87eb-dd790826c0a0.PNG)  
  
- 업로드한 폴더 번호 순서대로 개발이 진행되었음

### 음절 추출  
- openCV를 통해 ***이미지 전처리, 텍스트 라인 추출, 음절 추출***의 과정을 거쳤음  
![detection1](https://user-images.githubusercontent.com/65157567/96362644-b91f3300-1169-11eb-9ce9-c39e50497722.PNG)  
![detection2](https://user-images.githubusercontent.com/65157567/96362645-b9b7c980-1169-11eb-988a-079f12bc8f7c.PNG)  
### Font Classifier 개발
- 행정 문서에 가장 많이 등장하는 글씨체인 ***바탕, 돋움, 고딕, 명조 4가지의 군집***으로 분류  
- 바탕(11개), 돋움(6개), 고딕(14개), 명조(10개) 총 41개의 폰트를 이용해 폰트분류기를 개발  
  
![fc_1](https://user-images.githubusercontent.com/65157567/96362666-e4098700-1169-11eb-9235-52fd768abb83.PNG)  
![fc_2](https://user-images.githubusercontent.com/65157567/96362667-e53ab400-1169-11eb-8529-fd613792a4a1.PNG)  
### Tesseract 학습
- 로컬 개발 환경 : ***wsl2, ubuntu20.04***  

## 3. 결과
- ***NEW_Tesseract모듈 생성***  
- 행정문서 이미지가 input으로 들어왔을 때, ***폰트 분류기 이용과 이미지 전처리 여부*** 총 4가지의 경우로 문자를 추출할 수 있음  
- 폰트분류기를 거칠 경우, 행정문서에서 ***10개의 음절 중 확률이 높은 폰트***를 학습한 문자인식기를 거치게 됨  
- 폰트분류기를 사용함으로써 ***전체 개발 과정의 시간과 OCR속도를 높일 수 있다는 장점***이 있음  
  
![ocr](https://user-images.githubusercontent.com/65157567/96362574-41510880-1169-11eb-92b9-533202c0457b.PNG)  
