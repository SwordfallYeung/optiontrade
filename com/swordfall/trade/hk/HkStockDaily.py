import akshare as ak

stock_hk_daily_hfq_df = ak.stock_hk_daily(symbol="00981", adjust="hfq")

print(stock_hk_daily_hfq_df)