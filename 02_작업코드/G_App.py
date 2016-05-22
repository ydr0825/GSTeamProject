
def SearchWifi(InputGU, StartPage, EndPage):
    import urllib
    import http.client
    conn = http.client.HTTPConnection("openAPI.seoul.go.kr:8088")
    GuName = urllib.parse.quote(InputGU)
    conn.request("GET", "/6b4f54647867696c3932474d68794c/xml/PublicWiFiPlaceInfo/"+StartPage+"/"+EndPage+"/"+GuName)
    req = conn.getresponse() 
    print(req.status, req.reason)
    print(req.read().decode('utf-8'))
    

def main():
    s = input("검색하고자 하는 지역을 입력하세요: ")
    a, b = eval(input("범위를 입력해주세요: "))
    a = str(a)
    b = str(b)    
    SearchWifi(s, a, b)
