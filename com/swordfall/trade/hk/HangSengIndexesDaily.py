from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily

common_indexes_daily = CommonIndexesDaily()

def get_hk_hang_seng_index_daily(start_date, end_date):
    '''
    获取港股恒生指数指定日期内的每天行情
    :param start_date: 开始日期
    :param end_date: 结束日期
    :return:
    '''
    common_indexes_daily.get_index_daily(country="香港", index_name="恒生指数", start_date=start_date, end_date=end_date, method_name="get_hk_hang_seng_index_daily")



if __name__ == '__main__':
    get_hk_hang_seng_index_daily("2020-01-01","2020-08-02")