# -*- coding: utf-8 -*-
"""
@author: Ssenilen
"""

import http.client
from xml.dom.minidom import parse, parseString

BooksDoc = None
ItemNum = 1

### 검색 관련 함수
def SearchData(s):
    global ItemNum
    ItemNum = 1    
    
    if GetDocument(1, 800):
        PrintSearchData(s)    
  

        
def PrintSearchData(s):
    global BooksDoc
    if not checkDocument():
        return None
    
    parseData = parseString(BooksDoc)
    GeoInfoLibrary = parseData.childNodes
    row = GeoInfoLibrary[0].childNodes

    global ItemNum    
    
    for item in row:
        #print(item.nodeName)
        if item.nodeName == "row":
            subitems = item.childNodes
            
            if subitems[3].firstChild.nodeValue == s:  # 구 이름이 같을 경우
                pass
            elif subitems[5].firstChild.nodeValue == s:    # 동 이름이 같을 경우
                pass
            else:
                continue
            
            print(ItemNum, " - ", sep="", end="")
            if subitems[3].firstChild is not None: 
                print("구명: ", subitems[3].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[5].firstChild is not None: 
                print("동명: ", subitems[5].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[13].firstChild is not None: 
                print("새주소: ", subitems[13].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[15].firstChild is not None: 
                print("시설명: ", subitems[15].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[17].firstChild is not None: 
                print("운영기관: ", subitems[17].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[21].firstChild is not None: 
                print("시설구분: ", subitems[21].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[23].firstChild is not None: 
                print("개관일: ", subitems[23].firstChild.nodeValue, ", ", sep="", end="");
            if subitems[29].firstChild is not None: 
                print("연락처: ", subitems[29].firstChild.nodeValue, sep="", end="");
            print()
            
            ItemNum += 1


### 출력 관련 함수
def GetItemNum():   # 모든 항목의 수를 얻어온다.
    global ItemNum
    ItemNum = 1    
    
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    #GuName = urllib.parse.quote(InputGU)
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/1/1")
    req = conn.getresponse() 
    #print(req.status, req.reason)
    
    if req.status == 200:
        global BooksDoc 
        BooksDoc = req.read().decode('utf-8')
        #print("BooksDoc의 내용:"+BooksDoc)
        
        PrintSearchData(s)    
    else:
        print("해당 데이터를 읽어오는 데 실패했습니다.")    


### 기타 함수
def GetDocument(startNum, endNum):  # 해당 범위 내의 자료를 얻어온다. (startNum ~ endNum)
    startNum = int(startNum)
    endNum = int(endNum)
   
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/GeoInfoLibrary/"+startNum+"/"+endNum)
    req = conn.getresponse() 
   
    if req.status == 200:
        global BooksDoc 
        BooksDoc = req.read().decode('utf-8')
        return True   
    else:
        print("해당 데이터를 읽어오는 데 실패했습니다.")
        return False
    
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("에러 발생! 해당 문서는 비어있습니다.")
        return False
    return True

def Search():
    s = input("검색하고자 하는 지역을 입력하세요(구 또는 동): ")
    SearchData(s)  

    