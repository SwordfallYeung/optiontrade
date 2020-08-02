import akshare as ak
import time, datetime
import numpy as np
from com.swordfall.service.hk.HKStockService import HKStockService

hk_stock_service = HKStockService()

def get_hk_hang_seng_index_daily(start_date, end_date):
    hang_seng_index_daily_df = ak.index_investing_global("香港", index_name="恒生指数", period="每日", start_date=start_date, end_date=end_date)
    #print(hang_seng_index_daily_df)

    df_list_list = hang_seng_index_daily_df.values.__array__() if hang_seng_index_daily_df is not None else []
    df_date_list = hang_seng_index_daily_df.axes[0].array if hang_seng_index_daily_df is not None else []
    #print(tuple(df_list_list))
    #print(tuple(df_date_list))

    df_list_tuple = []
    for i in range(len(df_list_list)):
        lt = df_list_list[i]
        date = datetime.datetime.date(df_date_list[i])

        if np.isnan(lt[0]) == False:
            df_list_tuple.append((date, float(lt[0]), float(lt[1]), float(lt[2]), float(lt[3]), float(lt[4])))

        df_tuple_tuple = tuple(df_list_tuple)
    #print(df_tuple_tuple)
    flag = False
    try:
        flag = hk_stock_service.insert_index_daily_batch("恒生指数", df_tuple_tuple)
        print("恒生指数", flag)
    except Exception as ex:
        print("get_hk_hang_seng_index_daily exception, reason:", ex)

if __name__ == '__main__':
    get_hk_hang_seng_index_daily("2020-01-01","2020-08-02")