from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily
from datetime import datetime
import requests
import pandas as pd
from com.swordfall.service.hk.HKStockService import HKStockService

class HangSengIndexesDaily:

    def __init__(self):
        self.common_indexes_daily = CommonIndexesDaily()
        self.hk_stock_service = HKStockService()

    def get_hk_hang_seng_index_daily(self, start_date, end_date):
        '''
        获取港股恒生指数指定日期内的每天行情
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return:
        '''
        start_time = datetime.now()
        print("get_hk_hang_seng_index_daily 获取港股恒生指数指定日期内的每天行情 start_time:", start_time)

        self.common_indexes_daily.get_index_daily(country="香港", index_name="恒生指数", start_date=start_date, end_date=end_date,
                                             method_name="get_hk_hang_seng_index_daily")

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_hk_hang_seng_index_daily 获取港股恒生指数指定日期内的每天行情 end_time:", end_time, "耗时:", time)

    def update_hk_hang_seng_index_daily_lastest(self):
        '''
        更新港股恒生指数最新行情
        :return:
        '''
        start_time = datetime.now()
        print("update_hk_hang_seng_index_daily_lastest 更新港股恒生指数最新行情 start_time:", start_time)

        self.common_indexes_daily.update_index_daily_lastest(country="香港", index_name="恒生指数",
                                                        method_name="update_hk_hang_seng_index_daily_lastest")

        end_time = datetime.now()
        time = (end_time - start_time)
        print("update_hk_hang_seng_index_daily_lastest 更新港股恒生指数最新行情 end_time:", end_time, "耗时:", time)

    def get_hk_hang_seng_index_substock(self):
        start_time = datetime.now()
        print("get_hk_hang_seng_index_substock  start_time:", start_time)

        url = 'https://jpmhkwarrants.com/zh_hk/ajax/sector_hsi_hsce/type/hsi_top/order/6/desc/1'
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

        request = requests.get(url, headers=headers)
        data = pd.read_html(request.text)[0]

        sub_stocks_list = data['股票'].values

        index_substock_exist = self.get_hk_index_substock_exist()
        index_substock_exist_list = index_substock_exist.split(",")

        for stock in sub_stocks_list:
            symbol_name_arr = str(stock[0]).split(" ")
            if len(symbol_name_arr[0]) == 4:
                symbol_name_arr[0] = str(0) + symbol_name_arr[0]
            symbol_name = symbol_name_arr[0] + "_" + symbol_name_arr[1]
            print(symbol_name)

            if symbol_name not in index_substock_exist_list:
                index_substock_exist += symbol_name + ","

        self.update_hk_index_substock_list_exist(index_substock_exist, 'hk_index_substock_list', len(sub_stocks_list))

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_hk_hang_seng_index_substock end_time:", end_time, "耗时:", time)

    def get_hk_index_substock_exist(self):
        '''
        获取港股恒生指数成份股代码字符串
        :return:
        '''
        stock_exist = self.hk_stock_service.get_hk_stock_exist(5)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

    def update_hk_index_substock_list_exist(self, hk_stock_list_str, type, count):
        '''
        更新所有港股恒生指数成份股代码字符串
        :param hk_stock_list_str:
        :param count:
        :return:
        '''
        self.hk_stock_service.insert_or_update_hk_stock_exist(5, hk_stock_list_str, type, count)

if __name__ == '__main__':
    #get_hk_hang_seng_index_daily("2020-08-02","2020-08-02")
    hsid = HangSengIndexesDaily()
    #hsid.update_hk_hang_seng_index_daily_lastest()
    hsid.get_hk_hang_seng_index_substock()