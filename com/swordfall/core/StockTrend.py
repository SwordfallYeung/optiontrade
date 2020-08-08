
from com.swordfall.core.BaseTrend import BaseTrend

class StockTrend(BaseTrend):

    def stock_trend(self, stock_name):
        index_daily = self.commonStockService.select_batch("恒生指数", "2020-07-01", "2020-08-06")
        self.simple_judge(index_daily)
        print("---------------------------------------")
        #self.average_judge(index_daily)

        self.mixing_judge(index_daily)

        # self.calculate_nearby_daily_status(index_daily)

if __name__ == '__main__':
    st = StockTrend()
    st.stock_trend("恒生指数")