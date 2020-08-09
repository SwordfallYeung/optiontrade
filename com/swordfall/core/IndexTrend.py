
from com.swordfall.core.BaseTrend import BaseTrend

class IndexTrend(BaseTrend):

    def index_trend(self, index_name):
        now_date = str(self.commonUtils.get_china_today_time())
        month_ago_date = str(self.commonUtils.get_month_ago_date())
        index_daily = self.commonStockService.select_index_batch(index_name, month_ago_date, now_date)
        self.simple_judge(index_daily)
        print("---------------------------------------")
        #self.average_judge(index_daily)

        self.mixing_judge(index_daily)

        # self.calculate_nearby_daily_status(index_daily)

if __name__ == '__main__':
    st = IndexTrend()
    st.index_trend("恒生指数")