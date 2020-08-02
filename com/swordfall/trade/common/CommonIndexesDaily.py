import akshare as ak
import time, datetime
import numpy as np
from com.swordfall.service.common.CommonStockService import CommonStockService


class CommonIndexesDaily:

    def __init__(self):
        self.common_stock_service = CommonStockService()

    def get_index_daily(self, country, index_name, start_date, end_date, method_name):
        index_daily_df = ak.index_investing_global(country=country, index_name=index_name, period="每日",
                                                   start_date=start_date, end_date=end_date)
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
        flag = False
        try:
            flag = self.common_stock_service.insert_index_daily_batch(index_name, df_tuple_tuple)
            print(index_name, flag)
        except Exception as ex:
            print(method_name + " exception, reason:", ex)