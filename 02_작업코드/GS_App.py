
from tkinter import *
from tkinter import font

import http.client
from xml.dom.minidom import parse, parseString

import http.client

import smtplib 
from email.mime.text import MIMEText 

import tkinter.messagebox

#윈도우 생성
g_Tk = Tk()

#윈도우 크기
g_Tk.geometry("400x600+750+200")

g_EmailTkCheck = False
DataList = []


def InitApp():
    
    InitTopText()
    InitSearchListBox()
    InitInputLabel()
    InitSearchButton()
    InitRenderText()
    InitSendEmailButton()
    
    InitSortListBox()
    InitSortButton()
    
    g_Tk.mainloop()
    
def InitSortListBox():
    global SortListBox
    SortListBoxScrollbar = Scrollbar(g_Tk)
    SortListBoxScrollbar.pack()
    SortListBoxScrollbar.place(x=150, y=160)
       
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    SortListBox = Listbox(g_Tk,  font = TempFont, activestyle = 'none', 
                            width = 10, height = 1, borderwidth = 12, relief = 'ridge',
                            yscrollcommand = SortListBoxScrollbar.set)
                               
    SortListBox.insert(1, "시설명")
    SortListBox.insert(2, "주소")
    SortListBox.insert(3, "연락처")
    SortListBox.pack()
    SortListBox.place(x=10, y=160)
       
    SortListBoxScrollbar.config(command=SortListBox.yview)
    
def InitSortButton():
    TempFont = font.Font(g_Tk, size=14, weight='bold', family = 'Consolas')
    SortButtonUp = Button(g_Tk, font = TempFont, text="오름차순",  command=SortButtonUpAction)
    SortButtonUp.pack()
    SortButtonUp.place(x=175, y=165)
    
    TempFont = font.Font(g_Tk, size=14, weight='bold', family = 'Consolas')
    SortButtonDown = Button(g_Tk, font = TempFont, text="내림차순",  command=SortButtonDownAction)
    SortButtonDown.pack()
    SortButtonDown.place(x=280, y=165)

def SortButtonUpAction():
    global SortListBox
    global DataList
    iSortIndex = SortListBox.curselection()[0]    #리스트박스 인덱스 가져오기
    
    RenderText.configure(state = 'normal')
    RenderText.delete(0.0, END) #이전 출력 텍스트 모두 삭제
    DataList.sort(key=lambda e : e[iSortIndex]) 
    for i in range(len(DataList)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i+1) 
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "시설명: ")
        RenderText.insert(INSERT, DataList[i][0])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "주소: ")
        RenderText.insert(INSERT, DataList[i][1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "연락처: ")
        RenderText.insert(INSERT, DataList[i][2])
        RenderText.insert(INSERT, "\n\n")        
    RenderText.configure(state = 'disabled')    
    
def SortButtonDownAction():
    global SortListBox
    global DataList
    iSortIndex = SortListBox.curselection()[0]    #리스트박스 인덱스 가져오기
    
    RenderText.configure(state = 'normal')
    RenderText.delete(0.0, END) #이전 출력 텍스트 모두 삭제
    DataList.sort(key=lambda e : e[iSortIndex], reverse=True) 
    for i in range(len(DataList)):
        RenderText.insert(INSERT, "[")
        RenderText.insert(INSERT, i+1) 
        RenderText.insert(INSERT, "] ")
        RenderText.insert(INSERT, "시설명: ")
        RenderText.insert(INSERT, DataList[i][0])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "주소: ")
        RenderText.insert(INSERT, DataList[i][1])
        RenderText.insert(INSERT, "\n")
        RenderText.insert(INSERT, "연락처: ")
        RenderText.insert(INSERT, DataList[i][2])
        RenderText.insert(INSERT, "\n\n")        
    RenderText.configure(state = 'disabled')    
    
def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[서울시 근린시설 검색APP]")
    MainText.pack()
    MainText.place(x=20)
        
def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)
       
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    SearchListBox = Listbox(g_Tk,  font = TempFont, activestyle = 'none', 
                            width = 10, height = 1, borderwidth = 12, relief = 'ridge',
                            yscrollcommand = ListBoxScrollbar.set)
                               
    SearchListBox.insert(1, "도서관")
    SearchListBox.insert(2, "모범음식점")
    SearchListBox.insert(3, "마트")
    SearchListBox.insert(4, "문화공간")
    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)
       
    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitInputLabel():
    global InputLabel     
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)
       
def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)
    
def InitSendEmailButton():
    TempFont = font.Font(g_Tk, size=18, weight='bold', family = 'Consolas')
    SendEmailButton = Button(g_Tk, font = TempFont, text="이메일 보내기", command=SendEmailAction)
    SendEmailButton.pack()
    SendEmailButton.place(x=190, y=50)
    
def SendEmailAction():
    InitInputEmailAdressLabelAndButton()
    
def InitInputEmailAdressLabelAndButton():
    global InputEmailAdressLabel     
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputEmailAdressLabel = Entry(g_Tk, font = TempFont, width = 24, borderwidth = 12, relief = 'ridge')
    InputEmailAdressLabel.pack()
    InputEmailAdressLabel.place(x=25, y=320)
    
    global SendEmailButton
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SendEmailButton = Button(g_Tk, font = TempFont, text="전송",  command=SendEmailButtonAction)
    SendEmailButton.pack()
    SendEmailButton.place(x=320, y=325)
    
def SendEmailButtonAction():
    global InputEmailAdressLabel
    global mailer 
    mailer= smtplib.SMTP("smtp.gmail.com", 587) 
    mailer.ehlo() 
    mailer.starttls() 
    mailer.ehlo() 
    mailer.login("pythonmailer2016@gmail.com", "1q2w3e4r1q2w3e4r") 
    SendMailTest(InputEmailAdressLabel.get())

def SendMailTest(mailaddress): 
     text = "[서울시 근린시설 APP에서 요청한 검색 결과입니다.]\n\n"
     for i in range(len(DataList)):
        text += "["
        text += str(i+1) 
        text += "] "
        text += "시설명: "
        text += DataList[i][0]
        text += "\n"
        text += "주소: "
        text += DataList[i][1]
        text += "\n"
        text += "연락처: "
        text += DataList[i][2]
        text += "\n\n"
        
     msg = MIMEText(text) 
     senderAddr = "pythonmailer2016@gmail.com" 
     recipientAddr = mailaddress 
      
     msg['Subject'] = "서울시 근린시설 APP에서 요청한 검색 결과" 
     msg['From'] = "서울시 근린시설 검색 APP" 
     msg['To'] = recipientAddr 
      
     global mailer 
     mailer.sendmail(senderAddr, [recipientAddr], msg.as_string()) 
     mailer.close() 
     
     InputEmailAdressLabel.destroy()
     SendEmailButton.destroy()
     
     StrTemp = mailaddress + "\n\n" + "메일 전송 성공!"
     tkinter.messagebox.showinfo("[서울시 근린시설 검색APP]", StrTemp)

def InitRenderText():
    global RenderText
    
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
            
    TempFont = font.Font(g_Tk, size=10, family = 'Consolas')
    RenderText = Text(g_Tk, width = 49, height = 27, borderwidth = 12, relief = 'ridge', yscrollcommand = RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state = 'disabled')
    
def SearchButtonAction():
    global SearchListBox
    
    RenderText.configure(state = 'normal')
    RenderText.delete(0.0, END) #이전 출력 텍스트 모두 삭제
    
    iSearchIndex = SearchListBox.curselection()[0]    #리스트박스 인덱스 가져오기
    
    if iSearchIndex == 0:   #도서관
        SearchLibrary()
    elif iSearchIndex == 1: #모범음식
        SearchGoodFoodService()
    elif iSearchIndex == 2: #마켓
        SearchMarket()
    elif iSearchIndex == 3:
       SearchCultural()
       
    RenderText.configure(state = 'disabled')
    
def SearchLibrary():
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/800")
    req = conn.getresponse() 

    global DataList
    DataList.clear()    
    
    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
             parseData = parseString(BooksDoc)
             GeoInfoLibrary = parseData.childNodes
             row = GeoInfoLibrary[0].childNodes
             
             for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes
            
                    if subitems[3].firstChild.nodeValue == InputLabel.get():  # 구 이름이 같을 경우
                        pass
                    elif subitems[5].firstChild.nodeValue == InputLabel.get():    # 동 이름이 같을 경우
                        pass
                    else:
                        continue
                    
                    # 데이터 삽입 구간. 연락처가 없을 때에는 "-"을 넣는다.
                    if subitems[29].firstChild is not None:
                        tel = str(subitems[29].firstChild.nodeValue)
                        pass # 임시
                        if tel[0] is not '0':
                            tel = "02-" + tel    
                            pass
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))
             
             for i in range(len(DataList)):
                 RenderText.insert(INSERT, "[")
                 RenderText.insert(INSERT, i+1) 
                 RenderText.insert(INSERT, "] ")
                 RenderText.insert(INSERT, "시설명: ")
                 RenderText.insert(INSERT, DataList[i][0])
                 RenderText.insert(INSERT, "\n")
                 RenderText.insert(INSERT, "주소: ")
                 RenderText.insert(INSERT, DataList[i][1])
                 RenderText.insert(INSERT, "\n")
                 RenderText.insert(INSERT, "연락처: ")
                 RenderText.insert(INSERT, DataList[i][2])
                 RenderText.insert(INSERT, "\n\n")
                   
def SearchGoodFoodService():
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/ListGoodFoodService/1/800")
    req = conn.getresponse() 

    global DataList
    DataList.clear()    
    
    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
             parseData = parseString(BooksDoc)
             GeoInfoLibrary = parseData.childNodes
             row = GeoInfoLibrary[0].childNodes
             
             for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes
                    
                    s = subitems[13].firstChild.nodeValue.split()
                    if s[0] == InputLabel.get():  # 구 이름이 같을 경우
                        pass
                    elif s[1] == InputLabel.get():    # 동 이름이 같을 경우
                        pass
                    else:
                        continue
                    
                    if subitems[15].firstChild is not None:
                        tel = str(subitems[15].firstChild.nodeValue)
                        pass # 임시
                        if tel[0] is not '0':
                            tel = "02-" + tel          
                            pass
                        DataList.append((subitems[7].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[15].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))
                        
             for i in range(len(DataList)):       
                 RenderText.insert(INSERT, "[")
                 RenderText.insert(INSERT, i+1) 
                 RenderText.insert(INSERT, "] ")
                 RenderText.insert(INSERT, "시설명: ")
                 RenderText.insert(INSERT, DataList[i][0])
                 RenderText.insert(INSERT, "\n")
                 RenderText.insert(INSERT, "주소: ")
                 RenderText.insert(INSERT, DataList[i][1])
                 RenderText.insert(INSERT, "\n")
                 RenderText.insert(INSERT, "연락처: ")
                 RenderText.insert(INSERT, DataList[i][2])
                 RenderText.insert(INSERT, "\n\n")                     
                    
def SearchMarket():
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/ListMarketInfoServer/1/800")
    req = conn.getresponse() 

    global DataList
    DataList.clear()  
    
    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
             parseData = parseString(BooksDoc)
             GeoInfoLibrary = parseData.childNodes
             row = GeoInfoLibrary[0].childNodes
             
             for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes
                    
                    s = subitems[13].firstChild.nodeValue.split()
                    if s[0] == InputLabel.get():  # 구 이름이 같을 경우
                        pass
                    elif s[1] == InputLabel.get():    # 동 이름이 같을 경우
                        pass
                    else:
                        continue
                    
                    if subitems[11].firstChild is not None:
                        tel = str(subitems[11].firstChild.nodeValue)
                        pass # 임시
                        if tel[0] is not '0':
                            tel = "02-" + tel          
                            pass
                        DataList.append((subitems[9].firstChild.nodeValue, subitems[13].firstChild.nodeValue, tel))
                    else:
                        DataList.append((subitems[9].firstChild.nodeValue, subitems[13].firstChild.nodeValue, "-"))
                        
             for i in range(len(DataList)):       
                 RenderText.insert(INSERT, "[")
                 RenderText.insert(INSERT, i+1) 
                 RenderText.insert(INSERT, "] ")
                 RenderText.insert(INSERT, "시설명: ")
                 RenderText.insert(INSERT, DataList[i][0])
                 RenderText.insert(INSERT, "\n")
                 RenderText.insert(INSERT, "주소: ")
                 RenderText.insert(INSERT, DataList[i][1])
                 RenderText.insert(INSERT, "\n")
                 RenderText.insert(INSERT, "연락처: ")
                 RenderText.insert(INSERT, DataList[i][2])
                 RenderText.insert(INSERT, "\n\n")        

def SearchCultural():
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/SearchCulturalFacilitiesDetailService/1/800")
    req = conn.getresponse() 

    global DataList
    DataList.clear()  
    
    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
             parseData = parseString(BooksDoc)
             GeoInfoLibrary = parseData.childNodes
             row = GeoInfoLibrary[0].childNodes
             
             for item in row:
                if item.nodeName == "row":
                    subitems = item.childNodes
                    
                    dong = str("("+InputLabel.get()+")")
                    
                    s = subitems[11].firstChild.nodeValue.split()
                    for i in iter(s):
                        if i == InputLabel.get():     # 구나 동 이름이 동일할 때... 의 조건 1
                            bCheck = True
                            break
                        elif i == dong:         # 구나 동 이름이 동일할 때... 의 조건 2
                            bCheck = True
                            break
                        else:
                            bCheck = False
                    if bCheck:          
                        if subitems[13].firstChild is not None:
                            tel = str(subitems[13].firstChild.nodeValue)
                            pass # 임시
                            
                            if tel[0] is not '0':
                                tel = "02-" + tel          
                                pass
                            
                            DataList.append((subitems[7].firstChild.nodeValue, subitems[11].firstChild.nodeValue, tel))
                        else:
                            DataList.append((subitems[7].firstChild.nodeValue, subitems[11].firstChild.nodeValue, "-"))
                        
             for i in range(len(DataList)):       
                 RenderText.insert(INSERT, "[")
                 RenderText.insert(INSERT, i+1) 
                 RenderText.insert(INSERT, "] ")
                 RenderText.insert(INSERT, "시설명: ")
                 RenderText.insert(INSERT, DataList[i][0])
                 RenderText.insert(INSERT, "\n")
                 RenderText.insert(INSERT, "주소: ")
                 RenderText.insert(INSERT, DataList[i][1])
                 RenderText.insert(INSERT, "\n")
                 RenderText.insert(INSERT, "연락처: ")
                 RenderText.insert(INSERT, DataList[i][2])
                 RenderText.insert(INSERT, "\n\n")                
                    
InitApp()

         
         
         
         
         
         