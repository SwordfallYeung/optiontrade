import akshare as ak
from datetime import datetime
from com.swordfall.service.us.UStockService import UStockService
from com.swordfall.utils.CommonUtils import CommonUtils

class UstockList:

    def __init__(self):
        self.common_utils = CommonUtils()
        self.us_stock_service = UStockService()

    def get_ustock_list(self):
        '''
        获取所有美股信息
        :return:
        '''

        start_time = datetime.now()
        print("get_ustock_list 每天更新美股列表 start_time:", start_time)

        # pd.set_option('display.max_columns', None)  # 显示完整的列
        # pd.set_option('display.max_rows', None)  # 显示完整的行

        us_stock_current_df = ak.stock_us_spot()
        df_list = self.common_utils.dataframe_to_dict(us_stock_current_df)['data']
        # print(df_list)

        df_list_tuple = []
        stock_exist = self.get_us_stock_exist()
        stock_exist_list = stock_exist.split(",")

        for lt in df_list:
            symbol_name = lt[3]
            #print(symbol_name)
            if symbol_name not in stock_exist_list:
                stock_exist += symbol_name + ","
                name = str(lt[0]) if lt[0] is not None else ''
                cname = str(lt[1]) if lt[1] is not None else ''
                types = str(lt[2]) if lt[2] is not None else ''
                symbol = str(lt[3]) if lt[3] is not None else ''
                market = str(lt[15]) if lt[15] is not None else ''
                market_cap = int(lt[13]) if lt[13] is not None else 0
                # print((name, cname, type, symbol, market, market_cap))
                df_list_tuple.append((name, cname, types, symbol, market, market_cap))

        df_tuple_tuple = tuple(df_list_tuple)
        #print(df_tuple_tuple)
        flag = self.us_stock_service.insert_batch(df_tuple_tuple)
        # print(flag)
        if flag is True:
            self.update_us_stock_list_exist(stock_exist, 'us_stock_list', len(df_list))

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_ustock_list 每天更新美股列表 end_time:", end_time, "耗时:", time)

    def update_us_stock_list_exist(self, hk_stock_list_str, type, count):
        '''
        更新已存在的美股代码字符串
        :param hk_stock_list_str:
        :param count:
        :return:
        '''
        self.us_stock_service.insert_or_update_us_stock_exist(2, hk_stock_list_str, type, count)

    def get_us_stock_exist(self):
        '''
        更新美股代码字符串
        :return:
        '''
        stock_exist = self.us_stock_service.get_us_stock_exist(2)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

if __name__ == '__main__':
    utl = UstockList()
    utl.get_ustock_list()
    #stock_exist = get_us_stock_exist()
    #print("hello " + stock_exist)
