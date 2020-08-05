import akshare as ak
import time, datetime
import numpy as np
from com.swordfall.service.common.CommonStockService import CommonStockService
from com.swordfall.utils.CommonUtils import CommonUtils

class CommonIndexesDaily:

    def __init__(self):
        self.common_stock_service = CommonStockService()
        self.commonUtils = CommonUtils()

    def get_index_daily(self, country, index_name, start_date, end_date, method_name):
        '''
        获取指数一段时间内每天的行情
        :param country: 地区或者国家
        :param index_name: 指数名称
        :param start_date: 开始时间
        :param end_date: 结束时间
        :param method_name: 方法名称
        :return:
        '''
        try:
            index_daily_df = ak.index_investing_global(country=country, index_name=index_name, period="每日",
                                                   start_date=start_date, end_date=end_date)
        except Exception as ex:
            index_daily_df = None
            print("index_investing_global exception, reason:", ex)
        #print(index_daily_df)

        df_list_list = index_daily_df.values.__array__() if index_daily_df is not None else []
        df_date_list = index_daily_df.axes[0].array if index_daily_df is not None else []
        # print(tuple(df_list_list))
        # print(tuple(df_date_list))

        df_list_tuple = []
        for i in range(len(df_list_list)):
            lt = df_list_list[i]
            date = datetime.datetime.date(df_date_list[i])

            if np.isnan(lt[0]) == False:
                df_list_tuple.append((date, float(lt[1]), float(lt[2]), float(lt[3]), float(lt[0]), float(lt[4])))

        df_tuple_tuple = tuple(df_list_tuple)
        #print(df_tuple_tuple)
        if (len(df_tuple_tuple) > 0):
            flag = False
            try:
                flag = self.common_stock_service.insert_index_daily_batch(index_name, df_tuple_tuple)
                print(index_name, flag)
            except Exception as ex:
                print(method_name + " exception, reason:", ex)

    def update_index_daily_lastest(self, country, index_name, method_name):
        '''
        获取指数最新行情
        :param country: 国家或者地区
        :param index_name: 指数名称
        :param method_name: 方法名称
        :return:
        '''
        if country == "美国":
            time_now = self.commonUtils.get_us_today_time()
            #print("美国", time_now)
        elif country == "香港":
            time_now = self.commonUtils.get_china_hk_today_time()
            #print("香港", time_now)
        self.get_index_daily(country=country, index_name=index_name, start_date=str(time_now), end_date=str(time_now), method_name=method_name)