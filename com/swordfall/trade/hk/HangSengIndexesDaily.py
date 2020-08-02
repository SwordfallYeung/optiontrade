from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily

common_indexes_daily = CommonIndexesDaily()

def get_hk_hang_seng_index_daily(start_date, end_date):
   common_indexes_daily.get_index_daily(country="香港", index_name="恒生指数", start_date=start_date, end_date=end_date, method_name="get_hk_hang_seng_index_daily")

if __name__ == '__main__':
    get_hk_hang_seng_index_daily("2020-01-01","2020-08-02")