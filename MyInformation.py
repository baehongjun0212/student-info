# Hong Jun Bae

"""
사용 모듈 구성
"""
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser

class MyInformation: 
    def __init__(self): 
        self.root = Tk() 
        self.root.title("Student Information Program") 
        self.root.geometry("550x650") 
        self.root.resizable(width=False, height=False) 
        self.root.configure(bg="#BEB7A7")  
        
        """
        하위 메뉴 구성
        """
        self.menubar = Menu(self.root) 
        self.optionmenu = Menu(self.menubar, tearoff=0)  
        self.menubar.add_cascade(label="설정", menu=self.optionmenu) 
        self.optionmenu.add_command(label="입력 내용 초기화", command=self.content_init) 
        self.optionmenu.add_command(label="프로그램 종료", command=self.program_exit) 

        self.infomenu = Menu(self.menubar, tearoff=0) 
        self.menubar.add_cascade(label="정보", menu=self.infomenu)  
        self.infomenu.add_command(label="제작정보", command=self.make_info) 
        self.root.config(menu=self.menubar) 
        
        """
        학생 정보 엔트리 구성
        """
        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7") 
        self.spaceLabel.grid(row=0, column=0)
        
        self.infoLabel = Label(self.root, text="【 정보 입력 】",  fg='BLACK', bg='#BEB7A7', font=("Arial Bold", 15)) 
        self.infoLabel.grid(row=1, column=1)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7") 
        self.spaceLabel.grid(row=2, column=0)

        self.nameLabel = Label(self.root, text="이름", width=5, height=1,relief='groove', fg='white', bg='#5B5853', font=("NanumGothic", "12")) 
        self.nameLabel.grid(row=3, column=0)

        self.nameEntry = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10"))
        self.nameEntry.grid(row=3, column=1)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7") 
        self.spaceLabel.grid(row=4, column=0)

        self.ageLabel = Label(self.root, text="나이", width=5, height=1,relief='groove',fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.ageLabel.grid(row=5, column=0)

        self.ageEntry = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10"))
        self.ageEntry.grid(row=5, column=1)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7")
        self.spaceLabel.grid(row=6, column=0)

        self.numLabel1 = Label(self.root, text="학번", width=5, height=1,relief='groove',fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.numLabel1.grid(row=7, column=0)

        self.numEntry1 = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10")) 
        self.numEntry1.grid(row=7, column=1)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7") 
        self.spaceLabel.grid(row=8, column=0)

        self.numLabel2 = Label(self.root, text="학년", width=5, height=1,relief='groove',fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.numLabel2.grid(row=9, column=0)

        self.numEntry2 = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10")) 
        self.numEntry2.grid(row=9, column=1)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7") 
        self.spaceLabel.grid(row=10, column=0)

        self.majorLabel = Label(self.root, text="전공", width=5, height=1,relief='groove',fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.majorLabel.grid(row=11, column=0)

        self.majorEntry = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10"))
        self.majorEntry.grid(row=11, column=1)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7") 
        self.spaceLabel.grid(row=12, column=0)

        self.mailLabel = Label(self.root, text="이메일", width=5, height=1,relief='groove', fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.mailLabel.grid(row=13, column=0)

        self.mailEntry = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10")) 
        self.mailEntry.grid(row=13, column=1)
        
        """
        학생 정보-평균 학점 엔트리 구성
        """
        self.infoLabel = Label(self.root, text="【 평균 학점 】",fg='BLACK', bg='#BEB7A7', font=("Arial Bold", 15)) 
        self.infoLabel.grid(row=1, column=5)

        self.firstLabel = Label(self.root, text="1학년", width=5, height=1,relief='groove', fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.firstLabel.grid(row=3, column=4)

        self.firstEntry = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10")) 
        self.firstEntry.grid(row=3, column=5)

        self.secondLabel = Label(self.root, text="2학년", width=5, height=1,relief='groove', fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.secondLabel.grid(row=5, column=4)

        self.secondEntry = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10")) 
        self.secondEntry.grid(row=5, column=5)

        self.thirdLabel = Label(self.root, text="3학년",width=5, height=1,relief='groove', fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.thirdLabel.grid(row=7, column=4)

        self.thirdEntry = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10")) 
        self.thirdEntry.grid(row=7, column=5)

        self.fourthLabel = Label(self.root, text="4학년", width=5, height=1,relief='groove', fg='white', bg='#5B5853', font=("NanumGothic", "12"))
        self.fourthLabel.grid(row=9, column=4)

        self.fourthEntry = Entry(self.root, bg='#F0ECDD', relief='flat', font=("NanumGothic", "10")) 
        self.fourthEntry.grid(row=9, column=5)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7") 
        self.spaceLabel.grid(row=14, column=3)
        
        """
        기능 엔트리 구성
        """
        self.perLabel = Label(self.root, text="【 기능 】", fg='BLACK', bg='#BEB7A7', font=("Arial Bold", 15)) 
        self.perLabel.grid(row=15, column=4)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7")
        self.spaceLabel.grid(row=16, column=4)

        self.file_saveBtn = Button(self.root, text="입력 저장", command=self.saveFile, width=20, height=3,overrelief='solid',fg='white', bg='#7F867B', font=("NanumGothic", "10"))
        self.file_saveBtn.grid(row=17, column=1)

        self.file_printBtn = Button(self.root, text="입력 출력", command=self.printPop, width=20, height=3,overrelief='solid',fg='white', bg='#7F867B', font=("NanumGothic", "10"))
        self.file_printBtn.grid(row=17, column=5)

        self.graphBtn = Button(self.root, text="데이터 그래프", command=self.printGraph, width=20, height=3,overrelief='solid',fg='white', bg='#7F867B', font=("NanumGothic", "10"))
        self.graphBtn.grid(row=19, column=1)

        self.homepageBtn = Button(self.root, text="스마트 캠퍼스", command=self.goHomepage, width=20, height=3,overrelief='solid',fg='white', bg='#7F867B', font=("NanumGothic", "10"))
        self.homepageBtn.grid(row=19, column=5)

        self.spaceLabel = Label(self.root, text=" ", bg="#BEB7A7") 
        self.spaceLabel.grid(row=20, column=5)

        """
        하단 디자인 엔트리 구성
        """
        self.img = PhotoImage(file = "img.png")
        self.imageLabel = Label(self.root, image=self.img)
        self.imageLabel.grid(row=21, column=5)
        
        self.titleLabel = Label(self.root, text="2020 학생정보 프로그램" , fg='white', bg='#AF9F8C', font=("NanumGothic", 15))
        self.titleLabel.grid(row=23, column=5)

        """
        하위 메뉴 함수 구성
        """
    def content_init(self):
        self.nameEntry.delete(0, "end") # 이름 
        self.ageEntry.delete(0, "end") # 나이 
        self.numEntry1.delete(0, "end") # 학번 
        self.numEntry2.delete(0, "end") # 학년 
        self.majorEntry.delete(0, "end") # 전공 
        self.mailEntry.delete(0, "end") # 이메일 
        self.firstEntry.delete(0, "end") # 1학년 
        self.secondEntry.delete(0, "end") # 2학년 
        self.thirdEntry.delete(0, "end") # 3학년 
        self.fourthEntry.delete(0, "end") # 4학년

    def program_exit(self):
        self.root.destroy() 

    def make_info(self):
        messagebox.showinfo("제작 정보", "배홍준 제작")

        """
        학생 정보 함수
        """
    def changeScore(self, grade):
        if grade == "A+":
            return "100"
        elif grade == "A":
            return "90"
        elif grade == "B":
            return "80"
        elif grade == "C":
            return "70"

    def saveFile(self):
        name = self.nameEntry.get() # 이름
        age = self.ageEntry.get() # 나이
        number1 = self.numEntry1.get() # 학번
        number2 = self.numEntry2.get() # 학년
        major = self.majorEntry.get() # 전공
        mail = self.mailEntry.get() # 이메일

        first = self.changeScore(self.firstEntry.get())
        second = self.changeScore(self.secondEntry.get())
        third = self.changeScore(self.thirdEntry.get())
        fourth = self.changeScore(self.fourthEntry.get())
        
        filename = number1 + "_" + name + ".txt" 
        file = open(filename, "w") 

        file.write(name + " " + age + " " + number1 + " " + number2 + " " + major
                   + " " + mail + " " + first + " " + second + " " + third + " "
                   + fourth)
        file.close() 
        messagebox.showinfo("안내", "파일 저장이 완료 되었습니다!") 


    def printPop(self):
        name = self.nameEntry.get() # 이름
        age = self.ageEntry.get() # 나이
        number1 = self.numEntry1.get() # 학번
        number2 = self.numEntry2.get() # 학년
        major = self.majorEntry.get() # 전공
        mail = self.mailEntry.get() # 이메일

        first = self.changeScore(self.firstEntry.get()) 
        second = self.changeScore(self.secondEntry.get()) 
        third = self.changeScore(self.thirdEntry.get()) 
        fourth = self.changeScore(self.fourthEntry.get()) 

        newWindow = Toplevel(self.root)
        newWindow.title("출력") 
        newWindow.geometry("200x290") 
        newWindow.resizable(width=False, height=False)
        newWindow.configure(bg="#5B5853") 
        newWindow.attributes("-topmost", True) 
        messagebox.showinfo("안내", "입력 내용을 출력했습니다!") 
        
        spaceLabel = Label(newWindow,text="【학생 정보】",fg='white', bg="#5B5853", font=("NanumGothic", "12"))  
        spaceLabel.grid(row=0, column=0)

        nameLabel = Label(newWindow, text="이름 : "+name, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        nameLabel.grid(row=1, column=0, sticky=W)

        ageLabel = Label(newWindow, text="나이 : "+age, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        ageLabel.grid(row=3, column=0, sticky=W)

        numLabel1 = Label(newWindow, text="학번 : "+number1, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        numLabel1.grid(row=5, column=0, sticky=W)

        numLabel2 = Label(newWindow, text="학년 : "+number2, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        numLabel2.grid(row=7, column=0, sticky=W)

        majorLabel = Label(newWindow, text="전공 : "+major, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        majorLabel.grid(row=9, column=0, sticky=W)

        mailLabel = Label(newWindow, text="이메일 : "+mail, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        mailLabel.grid(row=11, column=0, sticky=W)

        spaceLabel = Label(newWindow,text="【평균 학점】",fg='white', bg="#5B5853", font=("NanumGothic", "12"))  
        spaceLabel.grid(row=12, column=0)

        firstLabel = Label(newWindow, text="1학년 : "+first, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        firstLabel.grid(row=13, column=0, sticky=W)

        secondLabel = Label(newWindow, text="2학년 : "+second, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        secondLabel.grid(row=15, column=0, sticky=W)

        thirdLabel = Label(newWindow, text="3학년 : "+third, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        thirdLabel.grid(row=17, column=0, sticky=W)

        fourthLabel = Label(newWindow, text="4학년 : "+fourth, width=25, height=1,fg='white', bg='#DDAFAD', font=("Arial Bold", "10"))
        fourthLabel.grid(row=19, column=0, sticky=W)

        spaceLabel = Label(newWindow,text="\"조금 더 분발합시다!\"",fg='white', bg="#5B5853", font=("NanumGothic", "9")) 
        spaceLabel.grid(row=20, column=0)

    """
    데이터 그래프 함수
    """        
    def printGraph(self):
        file = open("data_example.txt", "r") 
        datas = [[], [], [], [], [], [], [], [], []] 
        while True:  
            line = file.readline().strip() 
            if not line: 
                break 
            data = line.split("  ") 
            for i in range(9):
                datas[i].append(int(data[i]))  
        file.close() 
        x = range(10) 
        newWindow = Toplevel(self.root) 
        newWindow.title("Data Graph") 
        newWindow.geometry("1300x850") 
        newWindow.resizable(width=False, height=False) 
        
        global_fig = plt.figure(figsize=(15,15), dpi=100, facecolor='#F0ECDD')

        Ax = global_fig.add_subplot(5,3,1)
        Ax.set_title("[Ax] "+"Sum: "+str(sum(datas[0]))+" / Avg: "+str(sum(datas[0])/len(datas[0]))) #Ax
        Ax.plot(x, datas[0])
        
        Ay = global_fig.add_subplot(5,3,2)
        Ay.set_title("[Ay] "+"Sum: "+str(sum(datas[1]))+" / Avg: "+str(sum(datas[1])/len(datas[1]))) #Ay
        Ay.plot(x, datas[1])

        Az = global_fig.add_subplot(5,3,3)
        Az.set_title("[Az] "+"Sum: "+str(sum(datas[2]))+" / Avg: "+str(sum(datas[2])/len(datas[2]))) #Az
        Az.plot(x, datas[2])
       
        Bx = global_fig.add_subplot(5,3,7)
        Bx.set_title("[Bx] "+"Sum: "+str(sum(datas[3]))+" / Avg: "+str(sum(datas[3])/len(datas[3]))) #Bx
        Bx.plot(x, datas[3])
        
        By = global_fig.add_subplot(5,3,8)
        By.set_title("[By] "+"Sum: "+str(sum(datas[4]))+" / Avg: "+str(sum(datas[4])/len(datas[4]))) #By
        By.plot(x, datas[4])
  
        Bz = global_fig.add_subplot(5,3,9)
        Bz.set_title("[Bz] "+"Sum: "+str(sum(datas[5]))+" / Avg: "+str(sum(datas[5])/len(datas[5]))) #Bz
        Bz.plot(x, datas[5])
    
        Cx = global_fig.add_subplot(5,3,13)
        Cx.set_title("[Cx] "+"Sum: "+str(sum(datas[6]))+" / Avg: "+str(sum(datas[6])/len(datas[6]))) #Cx
        Cx.plot(x, datas[6])
   
        Cy = global_fig.add_subplot(5,3,14)
        Cy.set_title("[Cy] "+"Sum: "+str(sum(datas[7]))+" / Avg: "+str(sum(datas[7])/len(datas[7]))) #Cy
        Cy.plot(x, datas[7])
     
        Cz = global_fig.add_subplot(5,3,15)
        Cz.set_title("[Cz] "+"Sum: "+str(sum(datas[8]))+" / Avg: "+str(sum(datas[8])/len(datas[8]))) #Cz
        Cz.plot(x, datas[8])

        canvas = FigureCanvasTkAgg(global_fig, master=newWindow) 
        canvas.draw() 
        canvas.get_tk_widget().pack() 
        global_fig.canvas.draw() 

    def goHomepage(self):
        webbrowser.open("https://smart.hallym.ac.kr") 

sp = MyInformation()
