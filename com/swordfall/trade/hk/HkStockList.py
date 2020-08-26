import akshare as ak
from datetime import datetime
from com.swordfall.service.hk.HKStockService import HKStockService
from com.swordfall.utils.CommonUtils import CommonUtils

class HkStockList:

    def __init__(self):
        self.common_utils = CommonUtils()
        self.hk_stock_service = HKStockService()

    def get_hk_all_stock_list_daily(self):
        '''
        获取所有港股信息
        :return:
        '''
        start_time = datetime.now()
        print("get_hk_all_stock_list_daily 每天更新港股列表 start_time:", start_time)

        current_data_df = ak.stock_hk_spot()
        #print(current_data_df)

        df_list = self.common_utils.dataframe_to_dict(current_data_df)['data']

        df_list_tuple = []
        stock_exist = self.get_hk_stock_exist()
        stock_exist_list = stock_exist.split(",")

        for lt in df_list:
            symbol_name = lt[0] + "_" + lt[1]
            print(symbol_name)
            if symbol_name not in stock_exist_list:
                stock_exist += symbol_name + ","
                df_list_tuple.append(tuple(lt[0:4]))

        df_tuple_tuple = tuple(df_list_tuple)
        print(df_tuple_tuple)
        #flag = self.hk_stock_service.insert_batch(df_tuple_tuple)
        flag = True
        if flag is True:
            print(stock_exist)
            self.update_hk_stock_list_exist(stock_exist, 'hk_stock_list', len(df_list))

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_hk_all_stock_list_daily 每天更新港股列表 end_time:", end_time, "耗时:", time)

    def update_hk_stock_list_exist(self, hk_stock_list_str, type, count):
        '''
        更新所有港股股票代码字符串
        :param hk_stock_list_str:
        :param count:
        :return:
        '''
        self.hk_stock_service.insert_or_update_hk_stock_exist(1, hk_stock_list_str, type, count)

    def get_hk_stock_exist(self):
        '''
        获取港股所有股票代码字符串
        :return:
        '''
        stock_exist = self.hk_stock_service.get_hk_stock_exist(1)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

if __name__ == '__main__':
    #stock_exist = get_hk_stock_exist()
    #print("hello " + stock_exist)
    hsl = HkStockList()
    hsl.get_hk_all_stock_list_daily()
    #stock_hk_list_exist()
