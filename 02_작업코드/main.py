# -*- coding: utf-8 -*-
"""
@author: Ssenilen
"""

import ListGoodFoodService
import ListMarketInfoServer
import GeoInfoLibrary
import SearchCulturalFacilitiesDetailService

loopFlag = -1

def PrintMenu():
    print("[서울시 근린시설 검색 APP]")
    print(" 1. 도서관 검색")
    print(" 2. 안심/모범 음식점 검색")
    print(" 3. 마트 검색")
    print(" 4. 문화공간 검색")
    print(" 9. 프로그램 종료")


def SelectMenu(SelectKey):
    
    if SelectKey == '1':
        GeoInfoLibrary.main()
    elif SelectKey == '2':
        ListGoodFoodService.main()
    elif SelectKey == '3':
        ListMarketInfoServer.main()
    elif SelectKey == '4':
        SearchCulturalFacilitiesDetailService.main()
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