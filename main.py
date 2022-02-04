# import urllib.request as ureq
# from bs4 import BeautifulSoup
#
# def Collect(url):
#     request = ureq.Request(url)
#     response = ureq.urlopen(request)
#     if response.getcode() != 200:
#         return None
#     else:
#         return response
#
#
# url = input("수집할 URL:")
# result = Collect(url)
# html = BeautifulSoup(result, 'html.parser')
# print("제목:", html.title.text)
# print("내용:")
# print(html.text)


# WebRobot 클래스 정의하기
from CandidateSql import CandidateSql
from WebRobot import WebRobot

cnt = 0


def DoIt(url, depth, wp):
    global cnt
    cnt = cnt + 1
    print("{0}번째 페이지 {1},{2} 수집".format(cnt, url, depth))


# seed_url = input("https://finance.naver.com/")
seed_url = "https://finance.naver.com/"
print(seed_url)
CandidateSql.AddCandidate(seed_url, 0)
WebRobot.CollectTM(5, DoIt)
