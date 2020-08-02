from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily

common_indexes_daily = CommonIndexesDaily()

def get_us_indexes_daily(index_name, start_date, end_date):
    common_indexes_daily.get_index_daily(country="美国", index_name=index_name, start_date=start_date, end_date=end_date,
                                         method_name="get_us_indexes_daily" +"_" + index_name)

if __name__ == '__main__':
    get_us_indexes_daily("道琼斯指数","2020-01-01","2020-08-02")
    get_us_indexes_daily("标普500指数", "2020-01-01", "2020-08-02")
    get_us_indexes_daily("纳斯达克综合指数", "2020-01-01", "2020-08-02")