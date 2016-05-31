# -*- coding: utf-8 -*-
"""
@author: Ssenilen
"""

import http.client
from xml.dom.minidom import parse, parseString

BooksDoc = None
ItemNum = 1

def LoadXMLData(SearchData):
    global ItemNum
    ItemNum = 1    
    
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    #GuName = urllib.parse.quote(InputGU)
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/SearchCulturalFacilitiesDetailService/1/800")
    req = conn.getresponse() 
    #print(req.status, req.reason)
    if req.status == 200:
        global BooksDoc 
        BooksDoc = req.read().decode('utf-8')
        #print("BooksDoc의 내용:"+BooksDoc)
        
        PrintAllData(SearchData)    
    else:
        print("해당 데이터를 읽어오는 데 실패했습니다.")        
        

def PrintAllData(SearchData):
    global BooksDoc
    if not checkDocument():
        return None
    
    parseData = parseString(BooksDoc)
    SearchCulturalFacilitiesDetailService = parseData.childNodes
    row = SearchCulturalFacilitiesDetailService[0].childNodes

    global ItemNum    
    
    for item in row:
        #print(item.nodeName)
        if item.nodeName == "row":
            subitems = item.childNodes

            dong = str("("+SearchData+")")
            
            s = subitems[11].firstChild.nodeValue.split()
            for i in iter(s):
                if i == SearchData:     # 구나 동 이름이 동일할 때... 의 조건 1
                    bCheck = True
                    break
                elif i == dong:         # 구나 동 이름이 동일할 때... 의 조건 2
                    bCheck = True
                    break
                else:
                    bCheck = False
                    
                    
            if bCheck:
                print(ItemNum, " - ", sep="", end="")
                if subitems[5].firstChild is not None: 
                    print("분류: ", subitems[5].firstChild.nodeValue, ", ", sep="", end="");
                if subitems[7].firstChild is not None: 
                    print("문화공간명: ", subitems[7].firstChild.nodeValue, ", ", sep="", end="");
                if subitems[11].firstChild is not None: 
                    print("주소: ", subitems[11].firstChild.nodeValue, ", ", sep="", end="");
                if subitems[13].firstChild is not None: 
                    print("전화번호:", subitems[13].firstChild.nodeValue, sep="", end="");
                print()
                
            ItemNum += 1 


def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("에러 발생! 해당 문서는 비어있습니다.")
        return False
    return True

def main():
    s = input("검색하고자 하는 지역을 입력하세요(구 또는 동): ")
    LoadXMLData(s)