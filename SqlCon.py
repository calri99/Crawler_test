import pymssql


class SqlCon:
    # conn = pymssql.connect("127.0.0.1:1433","khkim","rlarlghd1@","WebSearchEngine")
    conn = pymssql.connect(
        server="127.0.0.1",
        port="1433",
        user="tester",
        password="rlarlghd1@",
        database="WebSearchEngine")
    @staticmethod
    def Cursor():
        return SqlCon.conn.cursor()
    @staticmethod
    def Close():
        SqlCon.conn.close()
    @staticmethod
    def Commit():
        SqlCon.conn.commit()


# conn = pymssql.connect(
#     server="127.0.0.1",
#     port="1433",
#     user="tester",
#     password="rlarlghd1@",
#     database="WebSearchEngine")
#
# # Connection 으로부터 Cursor 생성
# cursor = conn.cursor()
#
# # SQL문 실행
# # query = str.format("Insert into Candidate(url,depth) values('{0}',{1})",'url',1)
# # query = "SELECT url from Candidate"
# query = "Insert into Candidate(Id, url,depth) values(1, 'url', 1)"
# print(query)
# cursor.execute(query)
#
# query = "SELECT url from Candidate"
# print(query)
# cursor.execute(query)
#
# # 데이타 하나씩 Fetch하여 출력
# row = cursor.fetchone()
# while row:
#     print(row)
#     row = cursor.fetchone()
#
# # 연결 끊기
# conn.close()
