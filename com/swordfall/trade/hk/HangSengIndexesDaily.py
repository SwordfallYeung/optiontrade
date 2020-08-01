import akshare as ak

def get_hk_hang_seng_index_daily():
    hang_seng_index_df = ak.index_investing_global("香港", index_name="恒生指数", period="每日", start_date="2020-07-01", end_date="2020-08-02")
    print(hang_seng_index_df)

if __name__ == '__main__':
    get_hk_hang_seng_index_daily()