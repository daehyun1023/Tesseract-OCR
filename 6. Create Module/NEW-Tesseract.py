#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
import os
from time import time
import numpy as np
import pandas as pd
import argparse
import matplotlib as mpl
import matplotlib.pyplot as plt
import cv2
import tempfile
from PIL import Image
import sys
import random
from tensorflow.compat.v2.keras.models import model_from_json

# directory remove
import shutil
import random
try:
    from PIL import Image
except ImportError:
    import Image

# pytesseract 환경변수 설정
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# tessdata_dir_config  =  '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"' 

# BINARY_THREHOLD = 180
# image resize (A4 size)
# from img_resize import set_image_dpi


# In[2]:


def load_model():
    json_file = open("C:/Users/duadp/Test/model/xcep_model.json", "r")
    loaded_model_json = json_file.read()
    json_file.close()
    
    loaded_model = model_from_json(loaded_model_json)

    # model에 weight 로드하기
    weight = "C:/Users/duadp/Test/model/xcep_weight.h5"
    loaded_model.load_weights(weight)
    return loaded_model


# In[3]:


def set_image_dpi(file_path,file_name):
    im = Image.open(file_name)
    # 2480,3508은 A4용지 크기
    size = (2480, 3508)
    # A4 용지 크기로 resize
    im_resized = im.resize(size, Image.ANTIALIAS)
    # 임시 파일, 디렉토리 생성하는 과정인데 필요X
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
    temp_filename = temp_file.name
    im_resized.save(temp_filename, dpi=(300, 300))
    return temp_filename


# In[4]:


def chr_detection(image,Img_pre=False):
    # 이미지 전처리한 경우와 안한 경우 인풋이 달라서 각자 경우 나누어 줌
    if Img_pre==False:
        img=cv2.imread(image)
    else:
        img=image
#     img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     img_blur=cv2.GaussianBlur(img_gray,(5,5),0)
    large=img
    rgb=cv2.pyrDown(large)
#     rgb=large
    
    # 이미지 전처리 안한 경우는 Color가 BGR이기때문에 Gray로 바꿔야 함
    if Img_pre==False:
        small=cv2.cvtColor(rgb,cv2.COLOR_BGR2GRAY)
    else:
        small=rgb
        
    # kernel matrix 사각행렬로 만들어줌
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    # 모폴로지의 gradient 연산
    grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)
    # 이진화
    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    
    # findcontours 함수를 이용해 음절 찾기
    contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    img_for_class=rgb.copy()
    img_result=[]
    margin_pixel=0
    
    mask = np.zeros(bw.shape, dtype=np.uint8)
    
    
    for idx in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[idx])
        mask[y:y+h, x:x+w] = 0

        # img_result.append(img_for_class[y-margin_pixel : y+h+margin_pixel,
        #                      x-margin_pixel : x+w+margin_pixel])
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
        bi=float(w/h)
        if (w > 20 and h > 20) and w<35 and h<35 and r<0.8 and bi<1.1:
            # 높이 너비가 20~35사이에 있는 것들만 추출 (그래야 음절만 추출이 됨)
            # img_result에 추출된 음절들 append
            img_result.append(img_for_class[y-margin_pixel : y+h+margin_pixel,
                                            x-margin_pixel : x+w+margin_pixel])
            cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)
    
    
    return img_result
    


# In[5]:


def char_resize(chars,Img_pre):
    result=[]
    if Img_pre==False:
        for char in chars:
            result.append(cv2.resize(char,(71,71)))
            
    else:
        for char in chars:
            re_char = np.repeat(char[..., np.newaxis], 3, -1)
            result.append(cv2.resize(re_char,(71,71)))
            
    return result


# In[6]:


def font_classifier(chars,Img_pre):
#     폰트분류 모델 load
    model=load_model()
    
    # 음절크기 71*71로 resize
    chars=char_resize(chars,Img_pre)
    len_chars=len(chars)
    numbers=list(range(len_chars))
    # chars에서 10개 임의로 선택
    idx=random.sample(numbers,10)
    font_dic={'batang':0,'dotum':0,'gothic':0,'myeongjo':0}
    font_list=['batang','dotum','gothic','myeongjo']
    
    for i in idx:
        char=chars[i]
        char=char.reshape([1,71,71,3])
        y_pred=model.predict(char)
        y_pred=np.argmax(y_pred)
        font_dic[font_list[y_pred]]+=1
    
    cnt=0
    font=-1
    # 10개중에서 가장 많이 선택된 폰트를 사용
    for i in font_dic.keys():
        if font_dic[i]>cnt:
            cnt=font_dic[i]
            font=i
    
    return font
    
    


# In[16]:


def image_smoothening(img):
#     ret1, th1 = cv2.threshold(img, BINARY_THREHOLD, 255, cv2.THRESH_BINARY)
    ret1, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    blur = cv2.GaussianBlur(th1, (3, 3), 0)
    ret2, th2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return th2

# 노이즈 제거하는 함수
def remove_noise_and_smooth(file_name):
    img = cv2.imread(file_name, 0)
    # threshold로 이진화
    filtered = cv2.adaptiveThreshold(img.astype(np.uint8), 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 41,3)
    # morphology 연산에 쓰일 kernel matrix 생성
    kernel = np.ones((1, 1), np.uint8)
    # 이진화된 이미지에 opening 작업 수행
    opening = cv2.morphologyEx(filtered, cv2.MORPH_OPEN, kernel)
    # opening 이미지에 closing 연산 수행
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    # 노이즈 
    img = image_smoothening(img)
    or_image = cv2.bitwise_or(img, closing)
    return or_image


### 이미지 전처리하는 함수 ( Img_pre=True)
def process_image_for_ocr(img,image_dir):
    # TODO : Implement using opencv
#     temp_filename = set_image_dpi(file_name)
    # image dpi 설정
    image=set_image_dpi(image_dir,img)
    # 노이즈 제거
    img_new = remove_noise_and_smooth(image)
    return img_new


# In[17]:


def image_to_txt(input_image,input_image_dir,FC=True,Img_pre=False):
    # input_image: 이미지 파일, FC=폰트 분류 여부, Img_pre=이미지 전처리 여부
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    trained_data_list=['batang','dotum'
                   ,'gothic','myeongjo','total']
    start_training_time=time()
    fonts={'batang':0,'dotum':1,'gothic':2,'myeongjo':3,'total':4}
    
    if Img_pre==False:
        # 이미지 전처리 안할경우 사이즈, dpi 설정
        resized_img=set_image_dpi(input_image_dir,input_image)
        
    else:
        # 이미지 전처리
        resized_img=process_image_for_ocr(input_image,input_image_dir)
    
    if FC==True:
        #폰트 분류할 경우 -> 분류된 폰트로 학습된 Tesseract 실행
        chars=chr_detection(resized_img,Img_pre)
        # 음절추출된 것들로 font 분류
        font=font_classifier(chars,Img_pre)
        
    else:
        #폰트 분류안할 경우 전체폰트로 학습시킨 Tesseract 실행
        font='total'
        
    # 이미지 전처리
    font_idx=fonts[font]
    
    
    trained_data=trained_data_list[font_idx]
    
    result=pytesseract.image_to_string(input_image,config='--psm 6 oem 3 -c preserve_interword_spaces=1',lang=trained_data)
    end_training_time=time()
                                       
    run_time=end_training_time-start_training_time
    print('Run time : ', run_time)
    print('=========================================')
    return result


# In[10]:


# set up your image directory 

# image_dir = 'C:/Users/duadp/Test/image/'
# os.chdir(image_dir)
# image_list = os.listdir(image_dir)
# image=image_list[0]


# In[14]:


# A=image_to_txt(image,image_dir,FC=False,Img_pre=False)


# In[56]:


# print(A)


# In[ ]:


# import sys
# sys.path.append('C:/Users/admin/Desktop/tesseract/module')
# sys.path


# In[ ]:


# sys.path.append('모듈 저장한 경로') 한 후 import
# sys.path.append('C:/Users/duadp/Test')
# sys.path


# In[ ]:


# if __name__ =='__main__':
#     asd

