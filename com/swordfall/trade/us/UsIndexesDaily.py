from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily

class UsIndexesDaily:

    def __init__(self):
        self.common_indexes_daily = CommonIndexesDaily()

    def get_us_indexes_daily(self, index_name, start_date, end_date):
        '''
        获取美股道琼斯指数、标普500指数、纳斯达克综合指数指定日期内的每天行情
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return:
        '''
        self.common_indexes_daily.get_index_daily(country="美国", index_name=index_name, start_date=start_date,
                                             end_date=end_date,
                                             method_name="get_us_indexes_daily" + "_" + index_name)

    def update_us_index_daily_lastest(self, index_name):
        '''
        更新美股指数最新行情
        :return:
        '''
        self.common_indexes_daily.update_index_daily_lastest(country="美国", index_name=index_name,
                                                        method_name="update_us_index_daily_lastest")

    def update_us_three_indexes_daily_lastest(self):
        '''
        更新美股美股道琼斯指数、标普500指数、纳斯达克综合指数最新行情
        :return:
        '''
        self.update_us_index_daily_lastest("道琼斯指数")
        self.update_us_index_daily_lastest("标普500指数")
        self.update_us_index_daily_lastest("纳斯达克综合指数")


if __name__ == '__main__':
    #get_us_indexes_daily("道琼斯指数","2020-01-01","2020-08-02")
    #get_us_indexes_daily("标普500指数", "2020-01-01", "2020-08-02")
    #get_us_indexes_daily("纳斯达克综合指数", "2020-01-01", "2020-08-02")
    uid = UsIndexesDaily()
    uid.update_us_three_indexes_daily_lastest()