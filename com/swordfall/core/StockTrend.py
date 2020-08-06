
from com.swordfall.service.common.CommonStockService import CommonStockService

class StockTrend:

    def __init__(self):
        self.commonStockService = CommonStockService()

    def index_up_trend(self, index_name):
        index_daily = self.commonStockService.select_batch("恒生指数", "2020-07-01", "2020-08-06")
        self.simple_judge(index_daily)
        print("---------------------------------------")
        #self.average_judge(index_daily)

        self.calculate_nearby_daily_status(index_daily)


    def simple_judge(self, index_daily):
        print("simple test:")
        for index in index_daily:
            date = index['date']
            open = index['open']
            close = index['close']

            if close > open:
                print(date, open, close, "up")
            if close < open:
                print(date, open, close, "down")

    def average_judge(self, index_daily):
        print("average test:")
        pre_index = 0
        for index in index_daily:
            date = index['date']
            open = index['open']
            close = index['close']
            average = (open + close) / 2
            if average > pre_index:
                print(date, average, "up")
            if average < pre_index:
                print(date, average, "down")
            pre_index = average

    def calculate_nearby_daily_status(self, index_daily):
        print("calculate_nearby_daily_status test:")

        calculate_status = {'status':'', 'count':0}
        for index in index_daily:
            date = index['date']
            open = index['open']
            close = index['close']

            status = calculate_status['status']

            if close > open:
                
                if status is not 'up':
                    calculate_status['status'] = 'up'
                    calculate_status['count'] = 1
                if status is 'up':
                    calculate_status['count'] = calculate_status['count'] + 1
            if close < open:

                if status is not 'down':
                    calculate_status['status'] = 'down'
                    calculate_status['count'] = 1
                if status is 'down':
                    calculate_status['count'] = calculate_status['count'] + 1
        print(calculate_status)

if __name__ == '__main__':
    st = StockTrend()
    st.index_up_trend("恒生指数")