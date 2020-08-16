import pandas as pd
import json
from datetime import datetime,timedelta

class CommonUtils:

    def dataframe_to_json(self, df : pd.DataFrame, orient = 'split' ):
        df_json = df.to_dict(orient = orient, force_ascii = False)
        return json.loads(df_json)

    def dataframe_to_dict(self, df : pd.DataFrame, orient = 'split' ):
        df_dict = df.to_dict(orient = orient)
        return df_dict

    def get_china_today_time(self):
        '''
        获取中国区时间
        :return:
        '''
        china_time = datetime.now().date()
        return china_time

    def get_china_hk_today_time(self):
        '''
        获取中国区香港时间
        :return:
        '''
        now_time = datetime.now()
        is_weekday = now_time.weekday()
        if is_weekday == 5:
            now_time = (now_time - timedelta(hours=24)).date()
            return now_time

        if is_weekday == 6:
            now_time = (now_time - timedelta(hours=48)).date()
            return now_time

        hour = now_time.hour
        min = now_time.minute
        if hour < 9 or (hour == 9 and min < 30):
            now_time = (now_time - timedelta(hours=24)).date()
            return now_time
        if (hour == 9 and min >= 30) or hour > 9:
            china_time = now_time.date()
            return china_time

    def get_china_hk_weekdays_time(self):
        '''
        获取中国区香港工作日时间
        :return:
        '''
        now_time = datetime.now()
        is_weekday = now_time.weekday()
        #print("now_time", now_time, 'is_weekday', is_weekday)
        if is_weekday == 5 or is_weekday == 6:
            return False

        hour = now_time.hour
        min = now_time.minute
        hour_min = hour * 60 + min
        #print("hour", hour, 'min', min, 'hour_min', hour_min)
        if hour_min >= 570 and hour_min <= 975:
            return True
        return False

    def get_us_today_time(self):
        '''
        获取美国区时间
        :return:
        '''
        china_time = datetime.now()
        us_time = (china_time - timedelta(hours=12))
        is_weekday = us_time.weekday()
        if is_weekday == 5:
            now_time = (us_time - timedelta(hours=24)).date()
            return now_time

        if is_weekday == 6:
            now_time = (us_time - timedelta(hours=48)).date()
            return now_time

        hour = us_time.hour
        min = us_time.minute
        if hour < 9 or (hour == 9 and min < 30):
            now_time = (us_time - timedelta(hours=24)).date()
            return now_time
        if (hour == 9 and min >= 30) or hour > 9:
            now_time = us_time.date()
            return now_time

        return us_time

    def get_us_weekdays_time(self):
        '''
        获取美国区工作日时间
        :return:
        '''
        china_time = datetime.now()
        us_time = (china_time - timedelta(hours=12))
        is_weekday = us_time.weekday()
        if is_weekday == 5 or is_weekday == 6:
            return False

        hour = us_time.hour
        min = us_time.minute
        hour_min = hour * 60 + min
        # print("hour", hour, 'min', min, 'hour_min', hour_min)
        if hour_min >= 570 and hour_min <= 960:
            return True
        return False

    def get_month_ago_date(self):
        '''
        获取前一个月的date 2020-08-09
        :return:
        '''
        china_time = datetime.now()
        month_ago_time = (china_time - timedelta(days=31)).date()
        return month_ago_time

if __name__ == '__main__':
    st = CommonUtils()
    # date = st.get_china_hk_today_time()
    # print(date)

    date = st.get_china_today_time()
    date2 = st.get_month_ago_date()

    print("date", date, ",", "date2", date2)

