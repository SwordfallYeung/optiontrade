from com.swordfall.service.hk.HKStockService import HKStockService
from com.swordfall.core.BaseTrend import BaseTrend

class StockTrend(BaseTrend):

    def __init__(self):
        super().__init__()
        self.hk_stock_service = HKStockService()

    def get_hk_stock_exist(self, id):
        '''
        获取港股所有股票代码字符串
        :return:
        '''
        stock_exist = self.hk_stock_service.get_hk_stock_exist(id)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

    def stock_trend(self, stock_name):
        now_date = str(self.commonUtils.get_china_today_time())
        month_ago_date = str(self.commonUtils.get_month_ago_date())
        stock_daily = self.commonStockService.select_stock_batch("hk_stock_daily", stock_name, month_ago_date, now_date)
        #self.simple_judge(stock_daily)
        #print("---------------stock_name: " + stock_name +"------------------------")
        #self.average_judge(index_daily)

        #self.mixing_judge(stock_daily)

        return self.calculate_nearby_daily_status(stock_daily)

    def substock_trend(self, substock_exist_list):
        for symbol_name in substock_exist_list:
            if len(symbol_name) > 0:
                symbol_name_array = symbol_name.split("_")
                symbol = symbol_name_array[0]
                name = symbol_name_array[1]
                calculate_status = self.stock_trend(symbol)
                if bool(calculate_status):
                    print('symbol', symbol, 'calculate_status', calculate_status, name)


    def all_stock_trend(self):
        # 获取所有港股代码字符串
        stock_exist = self.get_hk_stock_exist(1)
        stock_exist_list = stock_exist.split(',')

        print("------ 恒生指数 -------")
        hang_seng_substock_exist_list = self.get_hk_stock_exist(5).split(",")
        self.substock_trend(hang_seng_substock_exist_list)
        print("")

        print("------ 恒生中国企业指数 -------")
        hang_seng_guoqi_substock_exist_list = self.get_hk_stock_exist(9).split(",")
        self.substock_trend(hang_seng_guoqi_substock_exist_list)
        print("")

        print("------ 恒生科技指数 -------")
        hang_seng_tech_substock_exist_list = self.get_hk_stock_exist(10).split(",")
        self.substock_trend(hang_seng_tech_substock_exist_list)
        print("")

        print("------ 科技 -------")
        tech_substock_exist_list = self.get_hk_stock_exist(11).split(",")
        self.substock_trend(tech_substock_exist_list)
        print("")

        print("------ 地产 -------")
        estate_substock_exist_list = self.get_hk_stock_exist(12).split(",")
        self.substock_trend(estate_substock_exist_list)
        print("")

        print("------ 医疗/制药/保健 -------")
        medical_health_substock_exist_list = self.get_hk_stock_exist(13).split(",")
        self.substock_trend(medical_health_substock_exist_list)
        print("")

        print("------ 保险 -------")
        insurance_substock_exist_list = self.get_hk_stock_exist(14).split(",")
        self.substock_trend(insurance_substock_exist_list)
        print("")

        print("------ 银行 -------")
        bank_substock_exist_list = self.get_hk_stock_exist(15).split(",")
        self.substock_trend(bank_substock_exist_list)
        print("")

        print("------ 食品/饮品 -------")
        food_drink_substock_exist_list = self.get_hk_stock_exist(16).split(",")
        self.substock_trend(food_drink_substock_exist_list)
        print("")

        print("------ 纺织/服饰制造 -------")
        textile_clothes_substock_exist_list = self.get_hk_stock_exist(17).split(",")
        self.substock_trend(textile_clothes_substock_exist_list)
        print("")

        print("------ 工业 -------")
        industry_substock_exist_list = self.get_hk_stock_exist(18).split(",")
        self.substock_trend(industry_substock_exist_list)
        print("")

        print("------ 汽车 -------")
        car_substock_exist_list = self.get_hk_stock_exist(19).split(",")
        self.substock_trend(car_substock_exist_list)
        print("")

        print("------ 电子 -------")
        electronic_substock_exist_list = self.get_hk_stock_exist(20).split(",")
        self.substock_trend(electronic_substock_exist_list)
        print("")

        print("------ 证券/金融 -------")
        securities_finance_substock_exist_list = self.get_hk_stock_exist(21).split(",")
        self.substock_trend(securities_finance_substock_exist_list)
        print("")

        print("------ ETF/基金 -------")
        etf_fund_substock_exist_list = self.get_hk_stock_exist(22).split(",")
        self.substock_trend(etf_fund_substock_exist_list)
        print("")

        print("------ 电信服务 -------")
        telecommunication_substock_exist_list = self.get_hk_stock_exist(23).split(",")
        self.substock_trend(telecommunication_substock_exist_list)
        print("")

        print("------ 电力/燃气 -------")
        electricity_gas_substock_exist_list = self.get_hk_stock_exist(24).split(",")
        self.substock_trend(electricity_gas_substock_exist_list)
        print("")

        print("------ 博彩 -------")
        betting_substock_exist_list = self.get_hk_stock_exist(25).split(",")
        self.substock_trend(betting_substock_exist_list)

        print("------ 石油化工 -------")
        petrochemical_substock_exist_list = self.get_hk_stock_exist(26).split(",")
        self.substock_trend(petrochemical_substock_exist_list)
        print("")

        print("------ 建筑/建筑材料 -------")
        building_materials_substock_exist_list = self.get_hk_stock_exist(27).split(",")
        self.substock_trend(building_materials_substock_exist_list)
        print("")

        print("------ 金属 -------")
        metal_substock_exist_list = self.get_hk_stock_exist(28).split(",")
        self.substock_trend(metal_substock_exist_list)
        print("")

        print("------  饮食/酒店/旅游 -------")
        food_hotel_tourism_substock_exist_list = self.get_hk_stock_exist(29).split(",")
        self.substock_trend(food_hotel_tourism_substock_exist_list)
        print("")

        print("------ 航空 -------")
        aviation_substock_exist_list = self.get_hk_stock_exist(30).split(",")
        self.substock_trend(aviation_substock_exist_list)
        print("")


if __name__ == '__main__':
    st = StockTrend()
    #st.stock_trend("00700")
    st.all_stock_trend()