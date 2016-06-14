
from tkinter import *
from tkinter import font

import http.client
from xml.dom.minidom import parse, parseString

#윈도우 생성
g_Tk = Tk()

#윈도우 크기
g_Tk.geometry("400x600+100+100")    

import http.client

def InitApp():
    InitTopText()
    InitSearchListBox()
    InitInputLabel()
    InitSearchButton()
    InitRenderText()
    InitSendEmailButton()
    
    g_Tk.mainloop()
        
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
    InputLabel.place(x=10, y=120)
       
def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=125)
    
def InitSendEmailButton():
    TempFont = font.Font(g_Tk, size=18, weight='bold', family = 'Consolas')
    SendEmailButton = Button(g_Tk, font = TempFont, text="이메일 보내기")
    SendEmailButton.pack()
    SendEmailButton.place(x=190, y=50)
    
def InitRenderText():
    global RenderText
    
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
            
    TempFont = font.Font(g_Tk, size=10, family = 'Consolas')
    RenderText = Text(g_Tk, width = 49, height = 30, borderwidth = 12, relief = 'ridge', yscrollcommand = RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=180)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state = 'disabled')
    
def SearchButtonAction():
    
    Tk()
    
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
    
    ItemNum = 0
    
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
            
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, ItemNum) 
                    RenderText.insert(INSERT, "]")
                    RenderText.insert(INSERT, "시설명: ")
                    RenderText.insert(INSERT, subitems[15].firstChild.nodeValue)
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "주소: ")
                    RenderText.insert(INSERT, subitems[13].firstChild.nodeValue)
                    RenderText.insert(INSERT, "\n\n")
                        
                    ItemNum += 1  
def SearchGoodFoodService():
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/ListGoodFoodService/1/800")
    req = conn.getresponse() 
    
    ItemNum = 0
    
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
            
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, ItemNum) 
                    RenderText.insert(INSERT, "]")
                    RenderText.insert(INSERT, "시설명: ")
                    RenderText.insert(INSERT, subitems[7].firstChild.nodeValue)
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "주소: ")
                    RenderText.insert(INSERT, subitems[13].firstChild.nodeValue)
                    RenderText.insert(INSERT, "\n\n")
                        
                    ItemNum += 1  
                    
def SearchMarket():
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/ListMarketInfoServer/1/800")
    req = conn.getresponse() 
    
    ItemNum = 0
    
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

                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, ItemNum) 
                    RenderText.insert(INSERT, "]")
                    RenderText.insert(INSERT, "시설명: ")
                    RenderText.insert(INSERT, subitems[9].firstChild.nodeValue)
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "주소: ")
                    RenderText.insert(INSERT, subitems[13].firstChild.nodeValue)
                    RenderText.insert(INSERT, "\n\n")
                        
                    ItemNum += 1  

def SearchCultural():
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/SearchCulturalFacilitiesDetailService/1/800")
    req = conn.getresponse() 
    
    ItemNum = 0
    
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
                        RenderText.insert(INSERT, "[")
                        RenderText.insert(INSERT, ItemNum) 
                        RenderText.insert(INSERT, "]")
                        RenderText.insert(INSERT, "시설명: ")
                        RenderText.insert(INSERT, subitems[7].firstChild.nodeValue)
                        RenderText.insert(INSERT, "\n")
                        RenderText.insert(INSERT, "주소: ")
                        RenderText.insert(INSERT, subitems[11].firstChild.nodeValue)
                        RenderText.insert(INSERT, "\n\n")
                        
                        ItemNum += 1                    
                    
InitApp()

         
         
         
         
         
         