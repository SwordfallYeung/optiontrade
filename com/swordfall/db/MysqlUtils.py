import pymysql

class MysqlUtils:
    def __init__(self, host, port, user, password, db, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        self.conn = self.connectMysql()

        if(self.conn):
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def connectMysql(self):
        try:
            conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                   passwd=self.password, db=self.db, charset=self.charset,
                                   cursorclass=pymysql.cursors.DictCursor)
        except Exception:
            print("connect database failed")
            conn = False
        return conn

    def close(self):
        if(self.conn):
            try:
                if(type(self.cursor) == 'object'):
                    self.cursor.close()
                if(type(self.conn) == 'object'):
                    self.conn.close()
            except Exception:
                print("close database exception")

    def select_all(self, sql):
        res = ''
        if(self.conn):
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
            except Exception:
                res = False
                print("query database exception")
            self.close()
        return res

    def select_one(self, sql):
        res = ''
        if(self.conn):
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchone()
            except Exception:
                res = False
                print("query database exception")
            self.close()
        return res

    def update(self, sql):
        flag = False
        if(self.conn):
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                flag = True
            except Exception:
                self.conn.rollback()
                flag = False
                print("update database exception")
            self.close()
        return flag

    def delete(self, sql):
        flag = False
        if(self.conn):
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                flag = True
            except Exception:
                self.conn.rollback()
                flag = False
                print("update database exception")
            self.close()
        return flag
