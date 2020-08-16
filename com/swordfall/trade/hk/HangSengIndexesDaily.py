from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily
import datetime

class HangSengIndexesDaily:

    def __init__(self):
        self.common_indexes_daily = CommonIndexesDaily()

    def get_hk_hang_seng_index_daily(self, start_date, end_date):
        '''
        获取港股恒生指数指定日期内的每天行情
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return:
        '''
        start_time = datetime.now()
        print("get_hk_hang_seng_index_daily 获取港股恒生指数指定日期内的每天行情 start_time:", start_time)

        self.common_indexes_daily.get_index_daily(country="香港", index_name="恒生指数", start_date=start_date, end_date=end_date,
                                             method_name="get_hk_hang_seng_index_daily")

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_hk_hang_seng_index_daily 获取港股恒生指数指定日期内的每天行情 end_time:", end_time, "耗时:", time)

    def update_hk_hang_seng_index_daily_lastest(self):
        '''
        更新港股恒生指数最新行情
        :return:
        '''
        start_time = datetime.now()
        print("update_hk_hang_seng_index_daily_lastest 更新港股恒生指数最新行情 start_time:", start_time)

        self.common_indexes_daily.update_index_daily_lastest(country="香港", index_name="恒生指数",
                                                        method_name="update_hk_hang_seng_index_daily_lastest")

        end_time = datetime.now()
        time = (end_time - start_time)
        print("update_hk_hang_seng_index_daily_lastest 更新港股恒生指数最新行情 end_time:", end_time, "耗时:", time)

if __name__ == '__main__':
    #get_hk_hang_seng_index_daily("2020-08-02","2020-08-02")
    hsid = HangSengIndexesDaily()
    hsid.update_hk_hang_seng_index_daily_lastest()