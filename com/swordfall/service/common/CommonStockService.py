
import pandas as pd
from com.swordfall.db.MysqlUtils import MysqlUtils

class CommonStockService:

    def __init__(self):
        self.mysql_utils = MysqlUtils()

    def insert_index_daily_batch(self, index_name, df_tuple):
        '''
        批量插入某一股票代码的所有记录
        :param df_tuple: 元组
        :return:
        '''
        sql =  "replace into stock_index_daily(index_name, date, open, high, low, close, volume) \
                       values ('"+ index_name + "', %s, %s, %s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_tuple)

    def select_index_batch(self, index_name, start_date, end_date):
        '''
        获取某一指数或股票一段时间内的每天行情
        :param index_name: 指数名称
        :param start_date: 开始时间
        :param end_date: 结束时间
        :return:
        '''
        sql = "select date, open, high, low, close from stock_index_daily where " \
              "index_name = '%s' and date >= '%s' and date <= '%s'  " \
              "order by date asc" % (index_name, start_date, end_date)
        return self.mysql_utils.select_all(sql)

    def select_stock_batch(self, db, symbol_name, start_date, end_date):
        '''
        获取某一指数或股票一段时间内的每天行情
        :param index_name: 指数名称
        :param start_date: 开始时间
        :param end_date: 结束时间
        :return:
        '''
        sql = "select date, open, high, low, close from '%s' where " \
              "symbol = '%s' and date >= '%s' and date <= '%s'  " \
              "order by date asc" % (db, symbol_name, start_date, end_date)
        return self.mysql_utils.select_all(sql)