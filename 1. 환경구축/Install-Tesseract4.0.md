## 1. OCR이란?
~~~
- OCR : Optical Character Recognition, 광학 문자 인식  
- 사람이 쓰거나 기계로 인쇄한 문자를 이미지 스캐너로 획득하여 기계가 읽을 수 있는 문자로 변환하는 것
~~~

## 2. Tesseract 4.0  
### tesseract 3과의 차이점  
~~~
- tesseract 4.0의 경우, Linux 환경에서만 작동 가능하다.  
- 이미지를 문자로 인식할 때, 음절 단위가 아니라 하나의 라인 단위로 인식해 Box를 생성한다.  
~~~

### Training Process  
1. Tesseract 학습을 위해 데이터를 생성하는 2가지 방법  
    (1) .ttf 파일 + .training_text 이용  
    (2) 이미지 파일에 직접 라벨링 후 이용  
    
2. Tesseract 학습 3가지 방법  
    (1) Fine Tuning  
    (2) Top Layer 교체  
    (3) From Scratch (처음부터 학습 시키기)  

3. 학습에 대한 구조 이해 및 방법  
    (1) 학습을 위해서는 ***글자 이미지 파일***이 필요함.  
    (2) ***.box 파일***이 필요함.  
    (3) ***.unicharset 파일***을 생성한다.  
    위의 세 가지는 데이터를 생성하는 과정임.   
    ***.ttf***로 데이터를 생성하는 경우, [tessdoc](https://github.com/tesseract-ocr/tessdoc/blob/master/TrainingTesseract-4.00.md#using-tesstrainsh)의 ***Using tesstrain.sh***를 참고한다.  
    
    (4) (1)~(3)의 파일을 다 만들면 학습에 필요한 ***.lstmf 파일***을 생성한다.  
    (5) 학습을 마친 후, ***기존의 .traineddata***와 ***checkpoint***를 combine해서 ***newtraineddata***를 생성한다.  
    
4. 참고자료 링크  
* [tesseract-ocr github](https://github.com/tesseract-ocr)  
* [tessdocs](https://github.com/tesseract-ocr/tessdoc)  
* [tesseract 4.0 학습 과정](https://github.com/tesseract-ocr/tessdoc/blob/master/TrainingTesseract-4.00.md)  


## 3. Required packages for tesseract 4.0  
#### Leptonica 패키지  
~~~
$ sudo apt-get install libletonica-dev  
~~~

#### Tesseract 설치  
~~~
$ sudo apt install tesseract-ocr  
$ sudo apt install libtesseract-dev  
~~~

#### v.4.1 설치  
~~~
$ sudo add-apt-repository ppa:alex-p/tesseract-ocr  
$ sudo apt-get update  
$ sudo apt install tesseract-ocr  
~~~

#### Packages for training  
~~~
$ sudo apt-get install libicu-dev libpango1.0-dev libcairo2-dev  
$ sudo apt-get install g++ autoconf automake libtool pkg-config libpng-dev libjpeg8-dev libtiff5-dev zlib1g-dev  
~~~
