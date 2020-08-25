from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily
from datetime import datetime
import pandas as pd
import requests
from com.swordfall.service.us.UStockService import UStockService

class UsIndexesDaily:

    def __init__(self):
        self.common_indexes_daily = CommonIndexesDaily()
        self.us_stock_service = UStockService()

    def get_us_indexes_daily(self, index_name, start_date, end_date):
        '''
        获取美股道琼斯指数、标普500指数、纳斯达克综合指数指定日期内的每天行情
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return:
        '''
        start_time = datetime.now()
        print("get_us_indexes_daily 获取美股三大指数指定日期内的每天行情 start_time:", start_time)

        self.common_indexes_daily.get_index_daily(country="美国", index_name=index_name, start_date=start_date,
                                             end_date=end_date,
                                             method_name="get_us_indexes_daily" + "_" + index_name)

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_us_indexes_daily 获取美股三大指数指定日期内的每天行情 end_time:", end_time, "耗时:", time)

    def update_us_index_daily_lastest(self, index_name):
        '''
        更新美股指数最新行情
        :return:
        '''
        #start_time = datetime.now()
        #print("update_us_index_daily_lastest 更新美股指数最新行情 start_time:", start_time)

        self.common_indexes_daily.update_index_daily_lastest(country="美国", index_name=index_name,
                                                        method_name="update_us_index_daily_lastest")
        #end_time = datetime.now()
        #time = (end_time - start_time)
        #print("update_us_index_daily_lastest 每天更新美股三大指数行情 end_time:", end_time, "耗时:", time)

    def update_us_three_indexes_daily_lastest(self):
        '''
        更新美股美股道琼斯指数、标普500指数、纳斯达克综合指数最新行情
        :return:
        '''
        start_time = datetime.now()
        print("update_us_three_indexes_daily_lastest 每天更新美股三大指数行情 start_time:", start_time)

        self.update_us_index_daily_lastest("道琼斯指数")
        self.update_us_index_daily_lastest("标普500指数")
        self.update_us_index_daily_lastest("纳斯达克综合指数")

        end_time = datetime.now()
        time = (end_time - start_time)
        print("update_us_three_indexes_daily_lastest 每天更新美股三大指数行情 end_time:", end_time, "耗时:", time)

    def get_us_indexes_daily_substock(self, url, id, type):
        start_time = datetime.now()
        print("get_us_indexes_daily_substock start_time:", start_time)

        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

        request = requests.get(url, headers=headers)
        data = pd.read_html(request.text)[0]

        # 欄位『Symbol』就是股票代碼
        sub_stocks_list = data.Symbol.values

        index_substock_exist = self.get_us_index_substock_exist(id)
        index_substock_exist_list = index_substock_exist.split(",")

        for symbol_name in sub_stocks_list:

            if symbol_name not in index_substock_exist_list:
                index_substock_exist += symbol_name + ","

        self.update_us_index_substock_list_exist(id, index_substock_exist, type, len(sub_stocks_list))

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_us_indexes_daily_substock end_time:", end_time, "耗时:", time)

    def get_us_index_substock_exist(self, id):
        '''
        获取美股指数成份股代码字符串
        :return:
        '''
        stock_exist = self.us_stock_service.get_us_stock_exist(id)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

    def update_us_index_substock_list_exist(self, id, us_stock_list_str, type, count):
        '''
        更新所有美股指数成份股代码字符串
        :param us_stock_list_str:
        :param count:
        :return:
        '''
        self.us_stock_service.insert_or_update_us_stock_exist(id, us_stock_list_str, type, count)

if __name__ == '__main__':
    #get_us_indexes_daily("道琼斯指数","2020-01-01","2020-08-02")
    #get_us_indexes_daily("标普500指数", "2020-01-01", "2020-08-02")
    #get_us_indexes_daily("纳斯达克综合指数", "2020-01-01", "2020-08-02")
    uid = UsIndexesDaily()
    #uid.update_us_three_indexes_daily_lastest()
    #uid.get_us_indexes_daily_substock('https://www.slickcharts.com/sp500', 6, 'us_sp500_index_substock_list')
    uid.get_us_indexes_daily_substock('https://www.slickcharts.com/nasdaq100', 7, 'us_nasdaq100_index_substock_list')
    uid.get_us_indexes_daily_substock('https://www.slickcharts.com/dowjones', 8, 'us_dowjones_index_substock_list')