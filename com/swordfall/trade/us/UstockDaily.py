import akshare as ak
import time, datetime
import numpy as np
from com.swordfall.service.us.UStockService import UStockService
from com.swordfall.utils.CommonUtils import CommonUtils
from com.swordfall.trade.common.CommonBaseDaily import CommonBaseDaily

class UstockDaily(CommonBaseDaily):

    def __init__(self):
        self.common_utils = CommonUtils()
        self.us_stock_service = UStockService()

    def get_us_all_stock_daily(self):
        '''
        获取每一只美股的所有历史行情，不包含今天
        :return:
        '''
        # 获取所有美股代码字符串
        stock_exist = self.get_us_stock_exist()
        stock_exist_list = stock_exist.split(',')

        # 获取历史行情的所有美股代码字符串
        all_stock_daily_exist = self.get_us_all_stock_daily_exist()
        us_all_stock_daily_str = all_stock_daily_exist
        us_all_stock_daily_count = 0

        for symbol in stock_exist_list:
            # if symbol > '01858' and symbol < '02226':
            #     flag = us_stock_service.test(symbol)
            #     print(symbol, flag)

            # if symbol == 'FFR':
            if all_stock_daily_exist.find(symbol) < 0:
                # print(symbol)
                # 根据港股代码获取某一只美股的所有历史行情
                try:
                    stock_us_daily_df = ak.stock_us_daily(symbol=symbol)
                    # print(stock_us_daily_df, type(stock_us_daily_df))
                except Exception as e:
                    stock_us_daily_df = None
                    print(" stock_hk_daily_hfq_df exception, reason:", e)

                df_list_list = stock_us_daily_df.values.__array__() if stock_us_daily_df is not None else []
                df_date_list = stock_us_daily_df.axes[0].array if stock_us_daily_df is not None else []

                df_list_tuple = []
                for i in range(len(df_list_list)):
                    lt = df_list_list[i]
                    # print(tuple(lt))
                    date = datetime.datetime.date(df_date_list[i])
                    # print(bool(np.isnan(lt[0])))
                    # print(type(np.isnan(lt[0])))
                    if np.isnan(lt[0]) == False:
                        df_list_tuple.append(
                            (date, float(lt[0]), float(lt[1]), float(lt[2]), float(lt[3]), float(lt[4])))
                    #     print(df_list_tuple)

                df_tuple_tuple = tuple(df_list_tuple)
                # print(df_tuple_tuple)
                flag = False
                try:
                    flag = self.us_stock_service.insert_one_stock_all_daily_batch(symbol, df_tuple_tuple)
                    print(symbol, flag)
                except Exception as ex:
                    print("insert_stock_daily_batch exception, reason:", ex)
                if flag is True:
                    us_all_stock_daily_count += 1
                    us_all_stock_daily_str += symbol + ","

        # 更新港股历史行情所有港股代码字符串
        self.update_us_stock_daily_exist(us_all_stock_daily_str, 'us_stock_daily', us_all_stock_daily_count)

    def update_us_stock_daily_exist(self, us_stock_list_str, type, count):
        '''
        更新所有美股代码字符串
        :param hk_stock_list_str:
        :param count:
        :return:
        '''
        self.us_stock_service.insert_or_update_us_stock_exist(4, us_stock_list_str, type, count)

    def get_us_all_stock_daily_exist(self):
        '''
        获取历史行情的所有美股代码字符串
        :return:
        '''
        stock_exist = self.us_stock_service.get_us_stock_exist(4)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

    def update_us_all_stock_daily_lastest(self):
        '''
        更新美股所有股票代码每天的行情，延迟15分钟
        :return:
        '''
        current_data_df = ak.stock_us_spot()
        df_list = self.common_utils.dataframe_to_dict(current_data_df)['data']

        df_list_tuple = []
        date_str = ''

        ticktime = self.common_utils.get_us_today_time()
        date_str = str(ticktime)

        for lt in df_list:
            symbol = lt[3]
            # if symbol == '00001':
            open = lt[8] if lt[8] is not None else 0
            high = lt[9] if lt[9] is not None else 0
            low = lt[10] if lt[10] is not None else 0
            last_trade = lt[4] if lt[4] is not None else 0
            volume = lt[12] if lt[12] is not None else 0

            df_list_tuple.append(
                (symbol, ticktime, float(open), float(high), float(low), float(last_trade), float(volume)))
            # print(symbol, open, high, low, last_trade, volume, ticktime)

        df_tuple_tuple = tuple(df_list_tuple)
        flag = False
        try:
            flag = self.us_stock_service.insert_all_stock_daily_batch(df_tuple_tuple)
            print(date_str, flag)
        except Exception as ex:
            print("insert_stock_daily_batch exception, reason:", ex)

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

    def update_us_all_stock_point_day(self, oneday_str):
        '''
        更新每一只美股指定的某一天历史行情
        :return:
        '''
        # 获取所有美股代码字符串
        stock_exist = self.get_us_stock_exist()
        stock_exist_list = stock_exist.split(',')

        start_time = datetime.datetime.now()
        print("start_time", start_time)
        df_list_tuple = []
        i = 0
        for symbol in stock_exist_list:
            try:
                stock_us_daily_df = ak.stock_us_daily(symbol=symbol)
                # print(stock_us_daily_df, type(stock_us_daily_df))
            except Exception as e:
                stock_us_daily_df = None
                print(" stock_us_daily_df exception, reason:", e)

            df_list_list = stock_us_daily_df.values.__array__() if stock_us_daily_df is not None else []
            df_date_list = stock_us_daily_df.axes[0].array if stock_us_daily_df is not None else []

            count = len(df_date_list)

            if count > 0:
                oneday_list = oneday_str.split(',')
                for oneday in oneday_list:
                    # print('df_date_list', tuple(df_date_list))
                    # print('count', count)
                    last_date = datetime.datetime.date(df_date_list[count - 1])
                    # print('last_date', last_date)
                    onedate = self.exchange_oneday_to_date(oneday)
                    # print('onedate', onedate)
                    days = self.days_reduce(last_date, onedate)
                    if days >= 0:
                        onedate_index = count - 1 - days
                        # print('onedate_index', onedate_index)
                        ondedate_lt = df_list_list[onedate_index]
                        # print('ondedate_lt', tuple(ondedate_lt))
                        df_list_tuple.append((symbol, onedate, float(ondedate_lt[0]), float(ondedate_lt[1]),
                                              float(ondedate_lt[2]), float(ondedate_lt[3]), float(ondedate_lt[4])))
                        print(i, symbol, onedate, float(ondedate_lt[0]), float(ondedate_lt[1]), float(ondedate_lt[2]),
                              float(ondedate_lt[3]), float(ondedate_lt[4]))
                        i += 1
                        if i % 500 == 0:
                            df_tuple_tuple = tuple(df_list_tuple)
                            flag = False
                            try:
                                flag = self.us_stock_service.insert_all_stock_daily_batch(df_tuple_tuple)
                                df_list_tuple = []
                                print(oneday, flag, i)
                            except Exception as ex:
                                print("us_all_stock_point_day_update exception, reason:", ex)

        df_tuple_tuple = tuple(df_list_tuple)
        flag = False
        try:
            flag = self.us_stock_service.insert_all_stock_daily_batch(df_tuple_tuple)
            print(oneday, flag, i)
        except Exception as ex:
            print("us_all_stock_point_day_update exception, reason:", ex)
        end_time = datetime.datetime.now()
        print("end_time", end_time)
        time = (end_time - start_time)
        print("耗时", time)

    def get_one_us_stock(self, symbol):
        stock_us_daily_df = ak.stock_us_daily(symbol)
        print(stock_us_daily_df)

if __name__ == '__main__':
    #get_us_all_stock_daily()

    utd = UstockDaily()
    #utd.update_us_all_stock_daily_lastest()
    utd.update_us_all_stock_point_day("2020-08-03,2020-08-04,2020-08-05,2020-08-06,2020-08-07")

    # us_time = get_us_today_time()
    # print(us_time)

    #print(exchange_oneday_to_date('2020-07-27'))

    # first_day = exchange_oneday_to_date('2020-07-14')
    # second_day = exchange_oneday_to_date('2020-07-25')
    # days = days_reduce(first_day, second_day)
    # if days > 0 :
    #     print("正常")
    # else:
    #     print("不正常")
    # print(days)

    #update_us_all_stock_point_day('2020-07-29')

    #get_one_us_stock('IGLEU')

    # start_time = datetime.datetime.now()
    # time.sleep(2)
    # end_time = datetime.datetime.now()
    # time = (end_time - start_time)
    # print("耗时", time, "s")

