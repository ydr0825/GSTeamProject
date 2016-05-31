# -*- coding: utf-8 -*-
"""
Created on Fri May 27 23:02:08 2016

@author: Ssenilen
"""

#import urllib
import http.client
from xml.dom.minidom import parse, parseString
#from xml.etree import ElementTree

BooksDoc = None
ItemNum = 1

def LoadXMLData(SearchData):
    global ItemNum
    ItemNum = 1    
    
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    #GuName = urllib.parse.quote(InputGU)
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/ListGoodFoodService/1/800")
    req = conn.getresponse() 
    #print(req.status, req.reason)
    if req.status == 200:
        global BooksDoc 
        BooksDoc = req.read().decode('utf-8')
        #print("BooksDoc의 내용:"+BooksDoc)
        
        PrintAllData(SearchData)    
    else:
        print("해당 데이터를 읽어오는 데 실패했습니다.")        
   
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/ListGoodFoodService/801/1600")
    req = conn.getresponse() 
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
    ListGoodFoodService = parseData.childNodes
    row = ListGoodFoodService[0].childNodes

    global ItemNum    
    
    for item in row:
        #print(item.nodeName)
        if item.nodeName == "row":
            subitems = item.childNodes
            
            s = subitems[13].firstChild.nodeValue.split()
            if s[0] == SearchData:  # 구 이름이 같을 경우
                pass
            elif s[1] == SearchData:    # 동 이름이 같을 경우
                pass
            else:
                continue
            
                
            print("{0}. 인증분야: {1}, 업체명: {2}, 주소: {3}, 전화번호: {4}".format(
                ItemNum,
                subitems[5].firstChild.nodeValue,
                subitems[7].firstChild.nodeValue,
                subitems[13].firstChild.nodeValue,
                subitems[15].firstChild.nodeValue))
            ItemNum += 1
            
            
            #for atom in subitems:
            #    print(atom.firstChild.nodeValue)
 

def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("에러 발생! 해당 문서는 비어있습니다.")
        return False
    return True

def main():
    s = input("검색하고자 하는 지역을 입력하세요(구 또는 동): ")
    LoadXMLData(s)