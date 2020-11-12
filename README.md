# student-info
## 파이썬을 이용한 학생 정보 저장 GUI 프로그램

## 실행화면
<img width="546" alt="1g1g" src="https://user-images.githubusercontent.com/55692618/98943201-78c98f80-2532-11eb-870c-68a7bf620658.PNG">
<img width="971" alt="55555" src="https://user-images.githubusercontent.com/55692618/98943256-9139aa00-2532-11eb-9aea-9b02c5c4d490.PNG">

## 프로그램 레이아웃
* GUI의 정확한 엔트리 배열 위치를 구상하기 위해, 초기 화면을 스케치하고 레이아웃을 디자인했다. 
![레이아웃](https://user-images.githubusercontent.com/55692618/98837380-3cd8f080-2486-11eb-9f4f-53968293cf72.png)

## 프로그램 아키텍처
* 프로그램은 크게 학생 정보 저장과 정보 출력, 평균 학점 계산, 데이터 그래프, 홈페이지 이동 등으로 이루어져 있다.  
* canvas에 data_example.txt 파일의 각 열 데이터와 총합, 평균을 계산해 출력한다.
![프로그램 아키텍처](https://user-images.githubusercontent.com/55692618/98837390-3ea2b400-2486-11eb-8a12-f01b74f558b4.png)

## 사용 모듈

```
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
```