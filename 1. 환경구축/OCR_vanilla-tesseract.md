# OCR-project
Tesseract for OCR

## 기존의 OCR의 정확도

전체 정확도는 유의미할 정도로 높으나 특수문자 등 인식 못하는 문제  
단, 한글 인식이 아닌 점, 자료가 오래된 점 등을 고려  
한글의 경우 자,모음의 조합이기 때문에 인식이 더욱 어려움  
![table](https://user-images.githubusercontent.com/32162748/83996679-aca6f480-a997-11ea-801b-6ee9cc477f12.png)

## prototype v0.1 상세 내용
---------------------------
### Figure.1
### resize = (2480, 3508)
### gray scale
### noise reduction

<div>

![gray](https://user-images.githubusercontent.com/32162748/83997091-951c3b80-a998-11ea-832f-7e541f44fe06.png)
![gray_out](https://user-images.githubusercontent.com/32162748/83997098-964d6880-a998-11ea-9fe5-382ec0ea99a6.png)
</div>
Kor + ENG를 사용했음에도 영어가 잘 안 읽혀지는 현상 발생   

engtrainned.data의 경우에도 적당히 학습을 시켜서 merge할 필요성 존재  

--------------------------------------------------------------------
### Figure.2
### resize = (2480, 3508)
### threshold (adptivethreshold / medianBlur )
### noise reduction

<div>

![threshold](https://user-images.githubusercontent.com/32162748/83997099-96e5ff00-a998-11ea-8198-32571c670dd7.png)

![threshold_out](https://user-images.githubusercontent.com/32162748/83997101-98172c00-a998-11ea-920b-59fc847ca17a.png)
</div>

### prototype Version 0.1 모습
