
from com.swordfall.service.common.CommonStockService import CommonStockService

class StockTrend:

    def __init__(self):
        self.commonStockService = CommonStockService()

    def index_up_trend(self, index_name):
        index_daily = self.commonStockService.select_batch("恒生指数", "2020-07-01", "2020-08-04")
        for index in index_daily:
            date = index['date']
            open = index['open']
            close = index['close']

            if close > open:
                print(date, open, close, "up")
            if close < open:
                print(date, open, close, "down")
            #print(index)

if __name__ == '__main__':
    st = StockTrend()
    st.index_up_trend("恒生指数")