
import pandas as pd
from com.swordfall.db.MysqlUtils import MysqlUtils

class UStockService:

    def __init__(self):
        self.mysql_utils = MysqlUtils()

    def insert_one(self, symbol, name, cname, market):
        sql = "insert into us_stock_list(symbol, name, cname, market) \
               values ('%s', '%s', '%s', '%s')" % \
              (symbol, name, cname, market)
        self.mysql_utils.insert_or_update(sql)

    def insert_batch(self, df_dict):
        sql = "insert into us_stock_list(symbol, name, cname, market) \
                       values (%s, %s, %s, %s)"
        self.mysql_utils.insert_batch(sql, df_dict)

    def insert_or_update_us_stock_exist(self, symbolstr, count):
        sql = "replace into stock_list_exist(id, symbolstr, count) values (2, '%s', %s)" % (symbolstr, count)
        self.mysql_utils.insert_or_update(sql)

    def get_us_stock_exist(self):
        sql = "select symbolstr from stock_list_exist where id = 2"
        return self.mysql_utils.select_one(sql)