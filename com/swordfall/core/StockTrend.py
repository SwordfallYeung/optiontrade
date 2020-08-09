
from com.swordfall.core.BaseTrend import BaseTrend

class StockTrend(BaseTrend):

    def stock_trend(self, stock_name):
        now_date = str(self.commonUtils.get_china_today_time())
        month_ago_date = str(self.commonUtils.get_month_ago_date())
        stock_daily = self.commonStockService.select_stock_batch("hk_stock_daily", stock_name, month_ago_date, now_date)
        self.simple_judge(stock_daily)
        print("---------------------------------------")
        #self.average_judge(index_daily)

        self.mixing_judge(stock_daily)

        # self.calculate_nearby_daily_status(index_daily)

if __name__ == '__main__':
    st = StockTrend()
    st.stock_trend("00700")