
import urllib.request
import xml.etree.cElementTree as ET

def subper(sub):
    url="http://openapi.seoul.go.kr:8088/sample/xml/ListAvgOfSeoulAirQualityService/1/1/"
    
    tree = ET.ElementTree(file = urllib.request.urlopen(url))
    root = tree.getroot()
    
    return root
    
if __name__ == "__main__":
   url="http://openapi.gg.go.kr/UndergroundWaterConstruct?KEY=sample&pIndex=1&pSize=50&SIGUN_CD=41310"
   data = urllib.request.urlopen(url).read()

   print(data)