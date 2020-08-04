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

    def get_us_today_time(self):
        '''
        获取美国区时间
        :return:
        '''
        china_time = datetime.datetime.now()
        us_time = (china_time - datetime.timedelta(hours=12)).date()
        return us_time