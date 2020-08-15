import akshare as ak
from datetime import time, datetime
import numpy as np
from com.swordfall.service.hk.HKStockService import HKStockService
from com.swordfall.utils.CommonUtils import CommonUtils
from com.swordfall.trade.common.CommonBaseDaily import CommonBaseDaily

class HkStockDaily(CommonBaseDaily):

    def __init__(self):
        self.common_utils = CommonUtils()
        self.hk_stock_service = HKStockService()

    def get_hk_all_stock_daily(self):
        '''
        获取所有港股的历史行情，不包含今天
        :return:
        '''
        start_time = datetime.now()
        print("start_time", start_time)

        # 获取所有港股代码字符串
        stock_exist = self.hk_stock_service.get_hk_stock_exist(id=1)
        stock_exist_list = stock_exist.split(',')

        # 获取港股历史行情所有港股代码字符串
        all_stock_daily_exist = self.get_hk_all_stock_daily_exist()
        hk_all_stock_daily_str = all_stock_daily_exist
        hk_all_stock_daily_count = 0

        for symbol in stock_exist_list:
            # if symbol > '01858' and symbol < '02226':
            #     flag = hk_stock_service.test(symbol)
            #     print(symbol, flag)

            # if symbol == '00001':
            if all_stock_daily_exist.find(symbol) < 0:
                # print(symbol)
                # 根据港股代码获取某一只港股的所有历史行情
                try:
                    stock_hk_daily_df = ak.stock_hk_daily(symbol=symbol)
                    # print(stock_hk_daily_hfq_df, type(stock_hk_daily_df))
                except Exception as e:
                    stock_hk_daily_df = None
                    print(" stock_hk_daily_hfq_df exception, reason:", e)

                df_list_list = stock_hk_daily_df.values.__array__() if stock_hk_daily_df is not None else []
                df_date_list = stock_hk_daily_df.axes[0].array if stock_hk_daily_df is not None else []

                df_list_tuple = []
                for i in range(len(df_list_list)):
                    lt = df_list_list[i]
                    date = datetime.date(df_date_list[i])
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
                    flag = self.hk_stock_service.insert_one_stock_all_daily_batch(symbol, df_tuple_tuple)
                    print(symbol, flag)
                except Exception as ex:
                    print("insert_stock_daily_batch exception, reason:", ex)
                if flag is True:
                    hk_all_stock_daily_count += 1
                    hk_all_stock_daily_str += symbol + ","

        # 更新港股历史行情所有港股代码字符串
        self.update_hk_stock_daily_exist(hk_all_stock_daily_str, 'hk_stock_daily', hk_all_stock_daily_count)

        end_time = datetime.now()
        print("end_time", end_time)
        time = (end_time - start_time)
        print("耗时", time)

    def update_hk_stock_daily_exist(self, hk_stock_list_str, type, count):
        '''
        更新所有港股股票代码字符串
        :param hk_stock_list_str:
        :param count:
        :return:
        '''
        self.hk_stock_service.insert_or_update_hk_stock_exist(3, hk_stock_list_str, type, count)

    def get_hk_all_stock_daily_exist(self):
        '''
        获取港股所有股票历史行情方面的代码字符串
        :return:
        '''
        stock_exist = self.hk_stock_service.get_hk_stock_exist(3)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

    def update_hk_all_stock_daily_lastest(self):
        '''
        更新港股所有股票代码当前最新的行情，延迟15分钟
        :return:
        '''
        print("SchedulerJobs update_hk_all_stock_daily_lastest 更新所有港股今天行情 start")
        start_time = datetime.now()
        print("start_time", start_time)

        current_data_df = ak.stock_hk_spot()
        df_list = self.common_utils.dataframe_to_dict(current_data_df)['data']

        df_list_tuple = []
        date_str = ''

        for lt in df_list:
            symbol = lt[0]
            # if symbol == '00001':
            open = lt[6] if lt[6] is not None else 0
            high = lt[7] if lt[7] is not None else 0
            low = lt[8] if lt[8] is not None else 0
            last_trade = lt[4] if lt[4] is not None else 0
            volume = lt[9] if lt[9] is not None else 0

            ticktime = datetime.fromisoformat(lt[11]).date() if lt[11] is not None else datetime.now()
            # print(ticktime, type(ticktime))
            date_str = str(ticktime)

            df_list_tuple.append(
                (symbol, ticktime, float(open), float(high), float(low), float(last_trade), float(volume)))
            # print(symbol, open, high, low, last_trade, volume, ticktime)

        df_tuple_tuple = tuple(df_list_tuple)
        flag = False
        try:
            flag = self.hk_stock_service.insert_all_stock_daily_batch(df_tuple_tuple)
            print(date_str, flag)
        except Exception as ex:
            print("insert_stock_daily_batch exception, reason:", ex)

        end_time = datetime.now()
        print("end_time", end_time)
        time = (end_time - start_time)
        print("耗时", time)
        print("SchedulerJobs update_hk_all_stock_daily_lastest 更新所有港股今天行情 end")

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

    def update_hk_all_stock_point_day(self, oneday_str):
        '''
        更新每一只港股指定的某一天历史行情
        :return:
        '''
        start_time = datetime.now()
        print("start_time", start_time)

        # 获取所有港股代码字符串
        stock_exist = self.get_hk_stock_exist()
        stock_exist_list = stock_exist.split(',')

        df_list_tuple = []
        i = 0
        for symbol in stock_exist_list:
            #if symbol == '09969':
                try:
                    stock_hk_daily_df = ak.stock_hk_daily(symbol=symbol)
                    print(stock_hk_daily_df, type(stock_hk_daily_df))
                except Exception as e:
                    stock_hk_daily_df = None
                    print(" stock_us_daily_df exception, reason:", e)

                df_list_list = stock_hk_daily_df.values.__array__() if stock_hk_daily_df is not None else []
                df_date_list = stock_hk_daily_df.axes[0].array if stock_hk_daily_df is not None else []

                count = len(df_date_list)

                if count > 0:
                    oneday_list = oneday_str.split(',')
                    for oneday in oneday_list:
                        # print('df_date_list', tuple(df_date_list))
                        # print('count', count)
                        last_date = datetime.date(df_date_list[count - 1])
                        # print('last_date', last_date)
                        onedate = self.exchange_oneday_to_date(oneday)
                        # print('onedate', onedate)
                        days = self.days_reduce(last_date, onedate)
                        if days >= 0:
                            onedate_index = count - 1 - days
                            # print('onedate_index', onedate_index)
                            ondedate_lt = df_list_list[onedate_index]
                            # print('ondedate_lt', tuple(ondedate_lt))

                            df_list_tuple.append(
                                (symbol, onedate, float(ondedate_lt[0]), float(ondedate_lt[1]), float(ondedate_lt[2]),
                                 float(ondedate_lt[3]), float(ondedate_lt[4])))
                            print(symbol, onedate, float(ondedate_lt[0]), float(ondedate_lt[1]), float(ondedate_lt[2]),
                                  float(ondedate_lt[3]), float(ondedate_lt[4]))
                            i += 1
                            if i % 500 == 0:
                                df_tuple_tuple = tuple(df_list_tuple)
                                flag = False
                                try:
                                    flag = self.hk_stock_service.insert_all_stock_daily_batch(df_tuple_tuple)
                                    df_list_tuple = []
                                    print(oneday_str, flag, i)
                                except Exception as ex:
                                    print("update_hk_all_stock_point_day exception, reason:", ex)

        df_tuple_tuple = tuple(df_list_tuple)
        flag = False
        try:
            flag = self.hk_stock_service.insert_all_stock_daily_batch(df_tuple_tuple)
            print(oneday_str, flag, i)
        except Exception as ex:
            print("update_hk_all_stock_point_day exception, reason:", ex)
        end_time = datetime.now()
        print("end_time", end_time)
        time = (end_time - start_time)
        print("耗时", time)

if __name__ == '__main__':
    #get_hk_all_stock_daily()
    hksd = HkStockDaily()
    #hksd.update_hk_all_stock_daily_lastest()

    hksd.update_hk_all_stock_point_day('2020-08-05,2020-08-06,2020-08-07')