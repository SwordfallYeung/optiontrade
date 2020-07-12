import pandas as pd
import json

class CommonUtils:

    def dataframe_to_json(self, df : pd.DataFrame, orient = 'split' ):
        df_json = df.to_dict(orient = orient, force_ascii = False)
        return json.loads(df_json)

    def dataframe_to_dict(self, df : pd.DataFrame, orient = 'split' ):
        df_dict = df.to_dict(orient = orient)
        return df_dict