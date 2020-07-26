import pymysql

class MysqlUtils:
    def __init__(self, host = "127.0.0.1", port = 3306 , user = "root", password = "root", db = "option_trade", charset='utf8'):
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
        except Exception as ex:
            print("connect database failed, reason:" + ex)
            conn = False
        return conn

    def close(self):
        if(self.conn):
            try:
                if(type(self.cursor) == 'object'):
                    self.cursor.close()
                if(type(self.conn) == 'object'):
                    self.conn.close()
            except Exception as ex:
                print("close database exception, reason:" + ex)

    def select_all(self, sql):
        res = ''
        if(self.conn):
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
            except Exception as ex:
                res = False
                print("query database exception, reason:" + ex)
            self.close()
        return res

    def select_one(self, sql):
        res = ''
        if(self.conn):
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchone()
            except Exception as ex:
                res = False
                print("query database exception, reason:" + ex)
            self.close()
        return res

    def insert_or_update(self, sql):
        flag = False
        if(self.conn):
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                flag = True
            except Exception as ex:
                self.conn.rollback()
                flag = False
                print("insert or update database exception, reason: " + ex)
            self.close()
        return flag

    def insert_batch(self, sql, val):
        flag = False
        if(self.conn):
            try:
                self.cursor.executemany(sql, val)
                self.conn.commit()
                flag = True
            except Exception as ex:
                self.conn.rollback()
                flag = False
                print("update database exception, reason: " + ex)
            self.close()
        return flag

    def delete(self, sql):
        flag = False
        if(self.conn):
            try:
                self.cursor.execute(sql)
                self.conn.commit()
                flag = True
            except Exception as ex:
                self.conn.rollback()
                flag = False
                print("update database exception, reason:" + ex)
            self.close()
        return flag
