import akshare as ak
import pandas as pd
from com.swordfall.service.us.UStockService import UStockService
from com.swordfall.utils.CommonUtils import CommonUtils


common_utils = CommonUtils()
us_stock_service = UStockService()

def ustock():
    #pd.set_option('display.max_columns', None)  # 显示完整的列
    #pd.set_option('display.max_rows', None)  # 显示完整的行

    us_stock_current_df = ak.stock_us_spot()

    df_list = common_utils.dataframe_to_dict(us_stock_current_df)['data']
    #us_stock_current_df = ak.get_us_stock_name()
    print(df_list)

    df_list_tuple = []
    stock_exist = get_us_stock_exist()
    hk_stock_list_str = stock_exist

    # for lt in df_list:
    #     stock_symbol = lt[0]
    #     if stock_exist.find(stock_symbol) < 0:
    #         hk_stock_list_str += lt[0] + ","
    #         df_list_tuple.append(tuple(lt[0:4]))
    #
    # stock_us_list_exist_update(hk_stock_list_str, len(df_list))
    # df_tuple_tuple = tuple(df_list_tuple)
    # us_stock_service.insert_batch(df_tuple_tuple)

def stock_us_list_exist_update(hk_stock_list_str, count):
    us_stock_service.insert_or_update_us_stock_exist(hk_stock_list_str, count)

def get_us_stock_exist():
    stock_exist = us_stock_service.get_us_stock_exist()
    if stock_exist is None:
        return ""
    if type(stock_exist) is dict:
        return stock_exist.get('symbolstr')

if __name__ == '__main__':
    ustock()
