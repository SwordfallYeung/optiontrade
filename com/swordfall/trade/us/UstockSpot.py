import akshare as ak


def ustock():
    us_stock_current_df = ak.stock_us_spot()
    print(us_stock_current_df)


if __name__ == '__main__':
    ustock()
