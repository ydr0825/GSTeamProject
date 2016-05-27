# -*- coding: utf-8 -*-
"""
@author: Ssenilen
"""

import ListGoodFoodService

loopFlag = -1

def PrintMenu():
    print("[서울시 근린시설 검색 APP]")
    print(" 1. 공공화장실 검색")
    print(" 2. 도서관 검색")
    print(" 3. 안심/모범 음식점 검색")
    print(" 4. 마트 검색")
    print(" 5. 공원 검색")
    print(" 9. 프로그램 종료")


def SelectMenu(SelectKey):
    if SelectKey == '3':
        ListGoodFoodService.main()
    
    elif SelectKey == '9':
        global loopFlag
        loopFlag = 0
    else:
        pass

while (loopFlag < 0):
    PrintMenu()
    SelectKey = input("메뉴를 선택해주세요: ")
    SelectMenu(SelectKey)
else:
    print("프로그램을 종료합니다.")