
import pandas as pd
from com.swordfall.db.MysqlUtils import MysqlUtils

class HKStockService:

    def __init__(self):
        self.mysql_utils = MysqlUtils()

    def insert_one(self, symbol, name, engname, tradetype):
        '''
        插入一条数据
        :param symbol: 股票代码
        :param name: 股票名称
        :param engname:
        :param tradetype: 交易类型
        :return:
        '''
        sql = "insert into hk_stock_list(symbol, name, engname, tradetype) \
               values ('%s', '%s', '%s', '%s')" % \
              (symbol, name, engname, tradetype)
        return self.mysql_utils.insert_or_update(sql)

    def insert_batch(self, df_tuple):
        '''
        批量插入
        :param df_tuple: 元组
        :return:
        '''
        sql = "insert into hk_stock_list(symbol, name, engname, tradetype) \
                       values (%s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_tuple)

    def insert_or_update_hk_stock_exist(self, id, symbolstr, type, count):
        '''
        插入或者更新港股所有股票代码
        :param symbolstr: 所有港股股票代码字符串
        :param count: 港股数量
        :return:
        '''
        sql = "replace into stock_list_exist(id, symbolstr, type, count) values ('%s', '%s', '%s', %s)" % (id, symbolstr, type, count)
        return self.mysql_utils.insert_or_update(sql)

    def get_hk_stock_exist(self, id):
        '''
        获取港股所有代码字符串
        :return:
        '''
        sql = "select symbolstr from stock_list_exist where id = %s" % (id)
        return self.mysql_utils.select_one(sql)

    def get_hk_stock_by_symbol(self, symbol):
        '''
        获取港股所有代码字符串
        :return:
        '''
        sql = "select name from hk_stock_list where symbol = %s" % (symbol)
        return self.mysql_utils.select_one(sql)

    def insert_one_stock_all_daily_batch(self, symbol, df_tuple):
        '''
        批量插入某一港股代码的所有记录
        :param df_tuple: 元组
        :return:
        '''
        sql =  "insert into hk_stock_daily(symbol, date, open, high, low, close, volume) \
                       values ('"+ symbol + "', %s, %s, %s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_tuple)

    def insert_all_stock_daily_batch(self, df_tuple):
        '''
        批量插入所有港股代码的某一天记录
        :param df_tuple: 元组
        :return:
        '''
        sql =  "replace into hk_stock_daily(symbol, date, open, high, low, close, volume) \
                       values (%s, %s, %s, %s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_tuple)

    def test(self, symbol):
        '''
        测试hk_stock_daily表是否有重复数据
        :param df_tuple: 元组
        :return:
        '''
        sql =  "SELECT count(*) FROM `option_trade`.`hk_stock_daily` WHERE `symbol` = %s AND `date` = '2020-07-20'" % (symbol)
        return self.mysql_utils.select_one(sql)