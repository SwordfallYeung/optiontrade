from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily
from datetime import datetime
import requests
import pandas as pd
from com.swordfall.service.hk.HKStockService import HKStockService

class HangSengIndexesDaily:

    def __init__(self):
        self.common_indexes_daily = CommonIndexesDaily()
        self.hk_stock_service = HKStockService()

    def get_hk_hang_seng_index_daily(self, start_date, end_date):
        '''
        获取港股恒生指数指定日期内的每天行情
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return:
        '''
        start_time = datetime.now()
        print("get_hk_hang_seng_index_daily 获取港股恒生指数指定日期内的每天行情 start_time:", start_time)

        self.common_indexes_daily.get_index_daily(country="香港", index_name="恒生指数", start_date=start_date, end_date=end_date,
                                             method_name="get_hk_hang_seng_index_daily")

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_hk_hang_seng_index_daily 获取港股恒生指数指定日期内的每天行情 end_time:", end_time, "耗时:", time)

    def update_hk_hang_seng_index_daily_lastest(self):
        '''
        更新港股恒生指数最新行情
        :return:
        '''
        start_time = datetime.now()
        print("update_hk_hang_seng_index_daily_lastest 更新港股恒生指数最新行情 start_time:", start_time)

        self.common_indexes_daily.update_index_daily_lastest(country="香港", index_name="恒生指数",
                                                        method_name="update_hk_hang_seng_index_daily_lastest")

        end_time = datetime.now()
        time = (end_time - start_time)
        print("update_hk_hang_seng_index_daily_lastest 更新港股恒生指数最新行情 end_time:", end_time, "耗时:", time)

    def update_substock_exist(self, data, id, type):
        substock_exist = self.get_hk_index_substock_exist(id)
        substock_exist_list = substock_exist.split(",")

        for stock in data:
            symbol_name_arr = str(stock[0]).split(" ")
            if len(symbol_name_arr[0]) == 4:
                symbol_name_arr[0] = str(0) + symbol_name_arr[0]
            symbol_name = symbol_name_arr[0] + "_" + symbol_name_arr[1]
            print(symbol_name)

            if symbol_name not in substock_exist_list:
                substock_exist += symbol_name + ","

        self.update_hk_index_substock_list_exist(id, substock_exist, type, len(data))

    def get_hk_index_substock(self, url, id, type):
        start_time = datetime.now()
        print("get_hk_hang_seng_index_substock  start_time:", start_time)

        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

        request = requests.get(url, headers=headers)
        data = pd.read_html(request.text)[0]

        sub_stocks_list = data['股票'].values

        self.update_substock_exist(sub_stocks_list, id, type)

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_hk_hang_seng_index_substock end_time:", end_time, "耗时:", time)

    def get_hk_hang_seng_index_substock(self):
        self.get_hk_index_substock('https://jpmhkwarrants.com/zh_hk/ajax/sector_hsi_hsce/type/hsi_top/order/6/desc/1', 5, 'hk_hangseng_index_substock_list')
        self.get_hk_index_substock('https://jpmhkwarrants.com/zh_hk/ajax/sector_hsi_hsce/type/hsce_top/order/6/desc/1', 9, 'hk_guoqin_index_substock_list')
        self.get_hk_index_substock('https://jpmhkwarrants.com/zh_hk/ajax/custom_sector/order/4/desc/1', 10, 'hk_tech_index_substock_list')

    def get_hk_plate_substock(self):
        start_time = datetime.now()
        print("get_hk_plate_substock  start_time:", start_time)

        url = 'https://jpmhkwarrants.com/zh_hk/ajax/sector_hot_rise_drop/type/hot'
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

        request = requests.get(url, headers=headers)
        data = pd.read_html(request.text)
        tech_data = data[2]['龍頭股'].values                 # 科技
        self.update_substock_exist(tech_data, 11, 'hk_plate_tech_substock_list')

        estate_data = data[4]['龍頭股'].values               # 地产
        self.update_substock_exist(estate_data, 12, 'hk_plate_estate_substock_list')

        medical_health_data = data[6]['龍頭股'].values       # 医疗/制药/保健
        self.update_substock_exist(medical_health_data, 13, 'hk_plate_medical_health_substock_list')

        insurance_data = data[8]['龍頭股'].values            # 保险
        self.update_substock_exist(insurance_data, 14, 'hk_plate_insurance_substock_list')

        bank_data = data[10]['龍頭股'].values                # 银行
        self.update_substock_exist(bank_data, 15, 'hk_plate_bank_substock_list')

        food_drink_data = data[12]['龍頭股'].values          # 食品/饮品
        self.update_substock_exist(food_drink_data, 16, 'hk_plate_food_drink_substock_list')

        textile_clothes_data = data[14]['龍頭股'].values     # 纺织/服饰制造
        self.update_substock_exist(textile_clothes_data, 17, 'hk_plate_textile_clothes_substock_list')

        industry_data = data[16]['龍頭股'].values            # 工业
        self.update_substock_exist(industry_data, 18, 'hk_plate_industry_substock_list')

        car_data = data[18]['龍頭股'].values                 # 汽车
        self.update_substock_exist(car_data, 19, 'hk_plate_car_substock_list')

        electronic_data = data[20]['龍頭股'].values          # 电子
        self.update_substock_exist(electronic_data, 20, 'hk_plate_electronic_substock_list')

        securities_finance_data = data[22]['龍頭股'].values  # 证券/金融
        self.update_substock_exist(securities_finance_data, 21, 'hk_plate_securities_finance_substock_list')

        etf_fund_data = data[24]['龍頭股'].values            # ETF/基金
        self.update_substock_exist(etf_fund_data, 22, 'hk_plate_etf_fund_substock_list')

        telecommunication_data = data[26]['龍頭股'].values   # 电信服务
        self.update_substock_exist(telecommunication_data, 23, 'hk_plate_telecommunication_substock_list')

        electricity_gas_data = data[28]['龍頭股'].values     # 电力/燃气
        self.update_substock_exist(electricity_gas_data, 24, 'hk_plate_electricity_gas_substock_list')

        betting_data = data[30]['龍頭股'].values             # 博彩
        self.update_substock_exist(betting_data, 25, 'hk_plate_betting_substock_list')

        petrochemical_data = data[32]['龍頭股'].values       # 石油化工
        self.update_substock_exist(petrochemical_data, 26, 'hk_plate_petrochemical_substock_list')

        building_materials_data = data[34]['龍頭股'].values  # 建筑/建筑材料
        self.update_substock_exist(building_materials_data, 27, 'hk_plate_building_materials_substock_list')

        metal_data = data[36]['龍頭股'].values               # 金属
        self.update_substock_exist(metal_data, 28, 'hk_plate_metal_substock_list')

        food_hotel_tourism_data = data[38]['龍頭股'].values  # 饮食/酒店/旅游
        self.update_substock_exist(food_hotel_tourism_data, 29, 'hk_plate_ food_hotel_tourism_substock_list')

        aviation_data = data[40]['龍頭股'].values            # 航空
        self.update_substock_exist(aviation_data, 30, 'hk_plate_aviation_substock_list')

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_hk_plate_substock end_time:", end_time, "耗时:", time)

    def get_hk_index_substock_exist(self, id):
        '''
        获取港股恒生指数成份股代码字符串
        :return:
        '''
        stock_exist = self.hk_stock_service.get_hk_stock_exist(id)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

    def update_hk_index_substock_list_exist(self, id, hk_stock_list_str, type, count):
        '''
        更新所有港股恒生指数成份股代码字符串
        :param hk_stock_list_str:
        :param count:
        :return:
        '''
        self.hk_stock_service.insert_or_update_hk_stock_exist(id, hk_stock_list_str, type, count)

if __name__ == '__main__':
    #
    hsid = HangSengIndexesDaily()
    hsid.get_hk_hang_seng_index_daily("2020-08-19", "2020-08-28")
    #hsid.update_hk_hang_seng_index_daily_lastest()
    #hsid.get_hk_hang_seng_index_substock()
    #hsid.get_hk_plate_substock()