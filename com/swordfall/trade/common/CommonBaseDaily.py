import time, datetime

class CommonBaseDaily:

    def days_reduce(self, first_day, second_day):
        delta = first_day - second_day
        return delta.days

    def exchange_oneday_to_date(self, oneday):
        onedate = datetime.datetime.fromisoformat(oneday)
        return datetime.datetime.date(onedate)