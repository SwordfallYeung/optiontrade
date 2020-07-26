
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
        sql = "insert into us_stock_list(name, cname, type, symbol, market) \
                       values (%s, %s, %s, %s, %s)"
        return self.mysql_utils.insert_batch(sql, df_dict)

    def insert_or_update_us_stock_exist(self, symbolstr, count):
        '''
        插入或者更新已存在的记录
        :param symbolstr: 所有股票代码字符串
        :param count: 股票数量
        :return: 成功则返回股票代码字符串，失败返回false
        '''
        sql = "replace into stock_list_exist(id, symbolstr, count) values (2, '%s', %s)" % (symbolstr, count)
        return self.mysql_utils.insert_or_update(sql)

    def get_us_stock_exist(self):
        '''
        获取已存在的所有股票代码字符串
        :return: 字符串
        '''
        sql = "select symbolstr from stock_list_exist where id = 2"
        return self.mysql_utils.select_one(sql)