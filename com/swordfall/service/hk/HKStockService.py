
import pandas as pd
from com.swordfall.db.MysqlUtils import MysqlUtils

class HKStockService:

    def __init__(self):
        self.mysql_utils = MysqlUtils()

    def insert_one(self, symbol, name, engname, tradetype):
        sql = "insert into hk_stock_list(symbol, name, engname, tradetype) \
               values ('%s', '%s', '%s', '%s')" % \
              (symbol, name, engname, tradetype)
        self.mysql_utils.insert_or_update(sql)

    def insert_batch(self, df_json):
        sql = "insert into hk_stock_list(symbol, name, engname, tradetype) \
                       values (%s, %s, %s, %s)"
        self.mysql_utils.insert_batch(sql, df_json)

    def insert_or_update_hk_stock_exist(self, symbolstr, count):
        sql = "replace into hk_stock_list_exist(id, symbolstr, count) values (1, '%s', %s)" % (symbolstr, count)
        self.mysql_utils.insert_or_update(sql)

    def get_hk_stock_exist(self):
        sql = "select symbolstr from hk_stock_list_exist where id = 1"
        return self.mysql_utils.select_one(sql)