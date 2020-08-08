from com.swordfall.service.common.CommonStockService import CommonStockService

class BaseTrend:

    def __init__(self):
        self.commonStockService = CommonStockService()

    def simple_judge(self, index_daily):
        '''
        通过close大于或等于open来判断上涨或下跌
        :param index_daily:
        :return:
        '''
        print("simple test:")
        for index in index_daily:
            date = index['date']
            open = index['open']
            close = index['close']
            status = ""
            if close > open:
                status = "up"
            if close < open:
                status = "down"
            print(date, open, close, status)

    def average_judge(self, index_daily):
        '''
        通过(open+close)/2大于前一天的(open+close)/2来判断上涨还是下跌
        :param index_daily:
        :return:
        '''
        print("average test:")
        pre_count = 0
        for index in index_daily:
            date = index['date']
            open = index['open']
            close = index['close']
            average = (open + close) / 2
            status = ""
            if average > pre_count:
                status = "up"
            if average < pre_count:
                status = "down"
            print(date, average, status)
            pre_count = average

    def mixing_judge(self, index_daily):
        '''
        通过open 大于 close 以及 今天的close大于前一天的close来判断上涨或下跌
        :param index_daily:
        :return:
        '''
        print("mixing_judge test:")
        pre_count = 0
        pre_status = ""
        for index in index_daily:
            date = index['date']
            open = index['open']
            close = index['close']

            status = ""
            if close > open:
                status = "up"
            if close < open:
                if close > pre_count:
                    if pre_status is "up":
                        status = "up"
                    if pre_status is "down":
                        status = "down"
                if close < pre_count:
                    status = "down"
            print(date, open, close, status)
            pre_count = close
            pre_status = status

    def calculate_nearby_daily_status(self, index_daily):
        '''
        计算最近几天是连涨几天，抑或是连跌几天
        :param index_daily:
        :return:
        '''
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