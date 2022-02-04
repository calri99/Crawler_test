from SqlCon import SqlCon
from WebPage import WebPage
import pymssql


class WebPageSql:
    @staticmethod
    def AddPage(wpage):
        cursor = SqlCon.Cursor()
        query = str.format("insert into WebPage (title, url, description, mcnt) values('{0}', '{1}', '{2}', {3})",
                           wpage.title, wpage.url, wpage.description, wpage.mcnt)
        try:
            cursor.execute(query)
            SqlCon.Commit()
        except:
            return False
        else:
            return True
    @staticmethod
    def UpdateMCnt(url,mcnt):
        cursor = SqlCon.Cursor()
        query = str.format("update WebPage set mcnt={0} where (url='{1}')",mcnt,url)
        cursor.execute(query)
        SqlCon.Commit()
    @staticmethod
    def FindPageByWid(wid):
        cursor = SqlCon.Cursor()
        query = str.format("select title, url, description, mcnt from WebPage where (wid={0})",wid)
        cursor.execute(query)
        row = cursor.fetchone()
        return row
    @staticmethod
    def TotalDocumentCount():
        cursor = SqlCon.Cursor()
        query = "select count(*) from WebPage"
        cursor.execute(query)
        row = cursor.fetchone()
        return row[0]
    @staticmethod
    def FindWid(url):
        cursor = SqlCon.Cursor()
        query = str.format("select wid from WebPage where (url='{0}')",url)
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            return row[0]
        return 0