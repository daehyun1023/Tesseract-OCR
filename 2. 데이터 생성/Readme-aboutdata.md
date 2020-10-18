## 데이터 생성
#### 개요
  - 보안문제로 인해 계약서 대신 ***99개의 행정 문서***로 대체함  
  - hwp, docs, pdf의 확장자 문서 파일  
  - 데이터 생성에 사용한 [행정문서](https://drive.google.com/drive/folders/1Y9hzABUxqBmQp3XlI2TgIohINhqs3tNj)는 구글 드라이브로 첨부  
  - docs를 이미지로 변환하는 것은 실패  
  - 모든 확장자를 ***pdf***로 변환하고, python으로 이미지 파일로 변경했음  
  - dpi : 300 / size : 2480*3508  
  
#### 설치 및 과정
* pdf2image 패키지 설치  
```python
!pip install pdf2image  
```
* poppler-path 설치  
[poppler-path](https://stackoverflow.com/questions/18381713/how-to-install-poppler-on-windows)의 Latest binary를 변환할 파일이 있는 경로에 설치함.  

* 예시
![pdf_to_png](https://user-images.githubusercontent.com/65157567/95543558-d0f10b80-0a33-11eb-9d10-3bc9d6f608f9.PNG)
