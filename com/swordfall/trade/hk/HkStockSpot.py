import akshare as ak
from com.swordfall.service.hk.HKStockService import HKStockService
from com.swordfall.utils.CommonUtils import CommonUtils

common_utils = CommonUtils()
hk_stock_service = HKStockService()

def stock_hk_spot():
    current_data_df = ak.stock_hk_spot()
    # print(current_data_df)

    df_list = common_utils.dataframe_to_dict(current_data_df)['data']

    df_list_tuple = []
    stock_exist = get_hk_stock_exist()
    hk_stock_list_str = stock_exist

    for lt in df_list:
        stock_symbol = lt[0]
        if stock_exist.find(stock_symbol) < 0:
            hk_stock_list_str += lt[0] + ","
            df_list_tuple.append(tuple(lt[0:4]))

    stock_hk_list_exist_update(hk_stock_list_str, len(df_list))
    df_tuple_tuple = tuple(df_list_tuple)
    hk_stock_service.insert_batch(df_tuple_tuple)


def stock_hk_list_exist_update(hk_stock_list_str, count):
    hk_stock_service.insert_or_update_hk_stock_exist(hk_stock_list_str, count)

def get_hk_stock_exist():
    stock_exist = hk_stock_service.get_hk_stock_exist()
    if stock_exist is None:
        return ""
    if type(stock_exist) is dict:
        return stock_exist.get('symbolstr')

if __name__ == '__main__':
    #stock_exist = get_hk_stock_exist()
    #print("hello " + stock_exist)

    stock_hk_spot()
    #stock_hk_list_exist()
