#Candidate(수집대상)Sql 클래스 만들기
import pymssql
from SqlCon import SqlCon
from WebPageSql import WebPageSql


class CandidateSql:
    @staticmethod
    def AddCandidate(url,depth):
        cursor = SqlCon.Cursor()
        print(cursor)
        if WebPageSql.FindWid(url)!=0:
            return False
        # id = CandidateSql.GetCandateMaxID()
        # query = str.format("Insert into Candidate(id, url,depth) values({0},'{1}',{2})", id, url, depth)
        query = f'Insert into Candidate(url,depth) values("{url}", {depth})'
        # query = str.format("Insert into Candidate(url,depth) values('{0}',{1})", url, depth)
        print(query)
        try:
            cursor.execute(query)
            SqlCon.Commit()
            return True
        except:
            return False
    @staticmethod
    def GetCandateID():
        cursor = SqlCon.Cursor()
        query = str.format("select MIN(id) from Candidate")
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return 0
    @staticmethod
    def GetCandateMaxID():
        cursor = SqlCon.Cursor()
        query = str.format("select MIN(id) from Candidate")
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            print(f'row: {len(row)-1}')
            return row[len(row)-1]
        else:
            return 0
    @staticmethod
    def Remove(id):
        cursor = SqlCon.Cursor()
        query = str.format("delete from Candidate where id={0}",id)
        cursor.execute(query)
        SqlCon.Commit()
    @staticmethod
    def GetCandidate():
        id = CandidateSql.GetCandateID()
        if id == None or id==0:
            return "",-1
        cursor = SqlCon.Cursor()
        query = str.format("select url,depth from Candidate where id={0}",id)
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            CandidateSql.Remove(id)
            return row[0], row[1]
        else:
            return "",-1