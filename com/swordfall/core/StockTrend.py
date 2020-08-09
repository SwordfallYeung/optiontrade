from com.swordfall.service.hk.HKStockService import HKStockService
from com.swordfall.core.BaseTrend import BaseTrend

class StockTrend(BaseTrend):

    def __init__(self):
        super().__init__()
        self.hk_stock_service = HKStockService()

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

    def stock_trend(self, stock_name):
        now_date = str(self.commonUtils.get_china_today_time())
        month_ago_date = str(self.commonUtils.get_month_ago_date())
        stock_daily = self.commonStockService.select_stock_batch("hk_stock_daily", stock_name, month_ago_date, now_date)
        #self.simple_judge(stock_daily)
        print("---------------stock_name: " + stock_name +"------------------------")
        #self.average_judge(index_daily)

        #self.mixing_judge(stock_daily)

        self.calculate_nearby_daily_status(stock_daily)

    def all_stock_trend(self):
        # 获取所有港股代码字符串
        stock_exist = self.get_us_stock_exist()
        stock_exist_list = stock_exist.split(',')

        for symbol in stock_exist_list:
            self.stock_trend(symbol)


if __name__ == '__main__':
    st = StockTrend()
    st.stock_trend("00700")