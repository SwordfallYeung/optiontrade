
import pandas as pd
from com.swordfall.db.MysqlUtils import MysqlUtils

class CommonStockService:

    def __init__(self):
        self.mysql_utils = MysqlUtils()

    def insert_index_daily_batch(self, indexname, df_tuple):
        '''
        批量插入某一股票代码的所有记录
        :param df_tuple: 元组
        :return:
        '''
        sql =  "replace into stock_index_daily(indexname, date, open, high, low, close, volume) \
                       values ('"+ indexname + "', %s, %s, %s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_tuple)