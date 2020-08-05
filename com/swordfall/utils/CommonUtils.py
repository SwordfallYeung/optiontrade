import pandas as pd
import json
import datetime

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
        china_time = datetime.datetime.now().date()
        return china_time

    def get_china_hk_today_time(self):
        '''
        获取中国区香港时间
        :return:
        '''
        now_time = datetime.datetime.now()
        is_weekday = now_time.weekday()
        if is_weekday == 5:
            now_time = (now_time - datetime.timedelta(hours=24)).date()
            return now_time

        if is_weekday == 6:
            now_time = (now_time - datetime.timedelta(hours=48)).date()
            return now_time

        hour = now_time.hour
        min = now_time.minute
        if hour < 9 or (hour > 9 and min < 30):
            now_time = (now_time - datetime.timedelta(hours=24)).date()
            return now_time
        if hour > 9 and min >= 30:
            china_time = now_time.date()
            return china_time

    def get_us_today_time(self):
        '''
        获取美国区时间
        :return:
        '''
        china_time = datetime.datetime.now()
        us_time = (china_time - datetime.timedelta(hours=12)).date()
        return us_time

if __name__ == '__main__':
    st = CommonUtils()
    date = st.get_china_hk_today_time()
    print(date)