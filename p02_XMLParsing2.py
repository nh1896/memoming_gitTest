# -*- coding:utf-8 -*-
# id : wIAFHrXRO7dVsCgDriTw
# secret : OxxCX8cYs8
from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from time import sleep

def cut(t): # 타이틀에 붙어있는거 떼버립시다
    t = t.replace("<b>","[")
    t = t.replace("</b>", "]")
    return t

# https://openapi.naver.com/v1/search/movie.xml
# https://openapi.naver.com/v1/search/movie.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&genre=1" \
# X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 client id 값}
# X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 client secret 값}

# ㅋ -> %3a (톰캣에선 자동으로 해줬지만 여긴 없음)
q = quote(input("영화명 : "))

# 요청헤더
h = {"X-Naver-Client-Id" : "wIAFHrXRO7dVsCgDriTw",
     "X-Naver-Client-Secret" : "OxxCX8cYs8"}

hc = HTTPSConnection("openapi.naver.com")
hc.request("GET", "/v1/search/movie.xml?query=" + q, headers=h)

# HTTP통신해서 응답결과 콘솔에 출력
# XML파싱해서 콘솔에 출력
resBody = hc.getresponse().read()

# print(resBody.decode())
try:
    for p in fromstring(resBody).getiterator("item"):
        print(cut(p.find("title").text))
        print(cut(p.find("subtitle").text))
        print(cut(p.find("pubDate").text))
        print(cut(p.find("userRating").text))
        print("--------------")
finally:
    sleep(1000)




