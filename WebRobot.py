import urllib.request as ureq
from bs4 import BeautifulSoup
from CandidateSql import CandidateSql
from WebPage import WebPage
from WebPageSql import WebPageSql
import threading


class WebRobot:
    @staticmethod
    def Collect(url):
        request = ureq.Request(url)
        try:
            response = ureq.urlopen(request)
        except:
            return None
        else:
            if response.getcode() != 200:
                return None
            return response

    @staticmethod
    def CollectHtml(url):
        print(f'CollectHtml: {url}')
        response = WebRobot.Collect(url)
        try:
            html = BeautifulSoup(response, 'html.parser')
        except:
            return None
        else:
            return html

    @staticmethod
    def CollectTM(period, tm_callback):
        url, depth = CandidateSql.GetCandidate()
        print(f'CollectTM: {url}')
        res = WebRobot.CollectHtml(url)
        if res != None:
            wp = WebPage.MakeWebPage(url, res)
            if wp != None:
                WebPageSql.AddPage(wp)
                for surl in wp.links:
                    CandidateSql.AddCandidate(surl, depth + 1)
                if tm_callback != None:
                    tm_callback(url, depth, wp)
        timer = threading.Timer(period, WebRobot.CollectTM, [period, tm_callback])
        timer.start()