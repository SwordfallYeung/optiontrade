
import pandas as pd
from com.swordfall.db.MysqlUtils import MysqlUtils

class UStockService:

    def __init__(self):
        self.mysql_utils = MysqlUtils()

    def insert_one(self, symbol, name, cname, market):
        '''
        插入一条数据
        :param symbol: 股票代码
        :param name: 美股名称
        :param cname: 美股中文名
        :param market: 上市场所
        :return: 成功或者失败 true or false
        '''
        sql = "insert into us_stock_list(name, cname, type, symbol, market) \
               values ('%s', '%s', '%s', '%s', '%s')" % \
              (symbol, name, cname, market)
        return self.mysql_utils.insert_or_update(sql)

    def insert_batch(self, df_dict):
        '''
        批量插入数据
        :param df_dict: 元组
        :return: 成功或者失败 true or false
        '''
        sql = "insert into us_stock_list(name, cname, type, symbol, market, market_cap) \
                       values (%s, %s, %s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_dict)

    def insert_or_update_us_stock_exist(self, id, symbolstr, type, count):
        '''
        插入或者更新已存在的记录
        :param symbolstr: 所有股票代码字符串
        :param type: 记录类型
        :param count: 股票数量
        :return: 成功则返回股票代码字符串，失败返回false
        '''
        sql = "replace into stock_list_exist(id, symbolstr, type, count) values ('%s', \"%s\", '%s', %s)" % (id, symbolstr, type, count)
        return self.mysql_utils.insert_or_update(sql)

    def get_us_stock_exist(self, id):
        '''
        获取已存在的所有股票代码字符串
        :return: 字符串
        '''
        sql = "select symbolstr from stock_list_exist where id = %s" % (id)
        return self.mysql_utils.select_one(sql)

    def insert_one_stock_all_daily_batch(self, symbol, df_tuple):
        '''
        批量插入某一美股代码的所有记录
        :param df_tuple: 元组
        :return:
        '''
        sql =  "insert into us_stock_daily(symbol, date, open, high, low, close, volume) \
                       values ('"+ symbol + "', %s, %s, %s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_tuple)

    def insert_all_stock_daily_batch(self, df_tuple):
        '''
        批量插入所有美股代码的某一天记录
        :param df_tuple: 元组
        :return:
        '''
        sql = "replace into us_stock_daily(symbol, date, open, high, low, close, volume) \
                       values (%s, %s, %s, %s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_tuple)

    def test(self, symbol):
        '''
        批量插入所有美股代码的某一天记录
        :param df_tuple: 元组
        :return:
        '''
        sql = "SELECT count(*) FROM `option_trade`.`us_stock_daily` WHERE `symbol` = %s AND `date` = '2020-07-20'" % (symbol)
        return self.mysql_utils.select_one(sql)

    def get_us_stock_by_symbol(self, symbol):
        '''
        根据symbol获取美股的中文名
        :return:
        '''
        sql = "select cname from us_stock_list where symbol = \"%s\"" % (symbol)
        return self.mysql_utils.select_one(sql)

    def get_us_stock_with_type_and_market_cap(self, type, market_cap):
        '''
        根据symbol获取美股的中文名
        :return:
        '''
        sql = "select symbol, cname from us_stock_list where type = \"%s\" and market_cap >= %s" % (type, market_cap)
        return self.mysql_utils.select_all(sql)