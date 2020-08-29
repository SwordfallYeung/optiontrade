from com.swordfall.service.hk.HKStockService import HKStockService
from com.swordfall.service.us.UStockService import UStockService
from com.swordfall.core.BaseTrend import BaseTrend

class StockTrend(BaseTrend):

    def __init__(self):
        super().__init__()
        self.hk_stock_service = HKStockService()
        self.us_stock_service = UStockService()

    def get_stock_exist(self, id):
        '''
        获取港美股所有股票代码字符串
        :return:
        '''
        stock_exist = self.hk_stock_service.get_hk_stock_exist(id)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

    def hk_stock_trend(self, stock_name):
        now_date = str(self.commonUtils.get_china_today_time())
        month_ago_date = str(self.commonUtils.get_month_ago_date())
        stock_daily = self.commonStockService.select_stock_batch("hk_stock_daily", stock_name, month_ago_date, now_date)
        #self.simple_judge(stock_daily)
        #print("---------------stock_name: " + stock_name +"------------------------")
        #self.average_judge(index_daily)

        #self.mixing_judge(stock_daily)

        return self.calculate_nearby_daily_status(stock_daily)

    def hk_substock_trend(self, substock_exist_list):
        for symbol_name in substock_exist_list:
            if len(symbol_name) > 0:
                symbol_name_array = symbol_name.split("_")
                symbol = symbol_name_array[0]
                name = symbol_name_array[1]
                calculate_status = self.hk_stock_trend(symbol)
                if bool(calculate_status):
                    print('symbol', symbol, 'calculate_status', calculate_status, name)


    def hk_all_stock_trend(self):
        # 获取所有港股代码字符串
        # stock_exist = self.get_hk_stock_exist(1)
        # stock_exist_list = stock_exist.split(',')

        print("------ 恒生指数 -------")
        hang_seng_substock_exist_list = self.get_stock_exist(5).split(",")
        self.hk_substock_trend(hang_seng_substock_exist_list)
        print("")

        print("------ 恒生中国企业指数 -------")
        hang_seng_guoqi_substock_exist_list = self.get_stock_exist(9).split(",")
        self.hk_substock_trend(hang_seng_guoqi_substock_exist_list)
        print("")

        print("------ 恒生科技指数 -------")
        hang_seng_tech_substock_exist_list = self.get_stock_exist(10).split(",")
        self.hk_substock_trend(hang_seng_tech_substock_exist_list)
        print("")

        print("------ 科技 -------")
        tech_substock_exist_list = self.get_stock_exist(11).split(",")
        self.hk_substock_trend(tech_substock_exist_list)
        print("")

        print("------ 地产 -------")
        estate_substock_exist_list = self.get_stock_exist(12).split(",")
        self.hk_substock_trend(estate_substock_exist_list)
        print("")

        print("------ 医疗/制药/保健 -------")
        medical_health_substock_exist_list = self.get_stock_exist(13).split(",")
        self.hk_substock_trend(medical_health_substock_exist_list)
        print("")

        print("------ 保险 -------")
        insurance_substock_exist_list = self.get_stock_exist(14).split(",")
        self.hk_substock_trend(insurance_substock_exist_list)
        print("")

        print("------ 银行 -------")
        bank_substock_exist_list = self.get_stock_exist(15).split(",")
        self.hk_substock_trend(bank_substock_exist_list)
        print("")

        print("------ 食品/饮品 -------")
        food_drink_substock_exist_list = self.get_stock_exist(16).split(",")
        self.hk_substock_trend(food_drink_substock_exist_list)
        print("")

        print("------ 纺织/服饰制造 -------")
        textile_clothes_substock_exist_list = self.get_stock_exist(17).split(",")
        self.hk_substock_trend(textile_clothes_substock_exist_list)
        print("")

        print("------ 工业 -------")
        industry_substock_exist_list = self.get_stock_exist(18).split(",")
        self.hk_substock_trend(industry_substock_exist_list)
        print("")

        print("------ 汽车 -------")
        car_substock_exist_list = self.get_stock_exist(19).split(",")
        self.hk_substock_trend(car_substock_exist_list)
        print("")

        print("------ 电子 -------")
        electronic_substock_exist_list = self.get_stock_exist(20).split(",")
        self.hk_substock_trend(electronic_substock_exist_list)
        print("")

        print("------ 证券/金融 -------")
        securities_finance_substock_exist_list = self.get_stock_exist(21).split(",")
        self.hk_substock_trend(securities_finance_substock_exist_list)
        print("")

        print("------ ETF/基金 -------")
        etf_fund_substock_exist_list = self.get_stock_exist(22).split(",")
        self.hk_substock_trend(etf_fund_substock_exist_list)
        print("")

        print("------ 电信服务 -------")
        telecommunication_substock_exist_list = self.get_stock_exist(23).split(",")
        self.hk_substock_trend(telecommunication_substock_exist_list)
        print("")

        print("------ 电力/燃气 -------")
        electricity_gas_substock_exist_list = self.get_stock_exist(24).split(",")
        self.hk_substock_trend(electricity_gas_substock_exist_list)
        print("")

        print("------ 博彩 -------")
        betting_substock_exist_list = self.get_stock_exist(25).split(",")
        self.hk_substock_trend(betting_substock_exist_list)

        print("------ 石油化工 -------")
        petrochemical_substock_exist_list = self.get_stock_exist(26).split(",")
        self.hk_substock_trend(petrochemical_substock_exist_list)
        print("")

        print("------ 建筑/建筑材料 -------")
        building_materials_substock_exist_list = self.get_stock_exist(27).split(",")
        self.hk_substock_trend(building_materials_substock_exist_list)
        print("")

        print("------ 金属 -------")
        metal_substock_exist_list = self.get_stock_exist(28).split(",")
        self.hk_substock_trend(metal_substock_exist_list)
        print("")

        print("------  饮食/酒店/旅游 -------")
        food_hotel_tourism_substock_exist_list = self.get_stock_exist(29).split(",")
        self.hk_substock_trend(food_hotel_tourism_substock_exist_list)
        print("")

        print("------ 航空 -------")
        aviation_substock_exist_list = self.get_stock_exist(30).split(",")
        self.hk_substock_trend(aviation_substock_exist_list)
        print("")

    def us_stock_trend(self, stock_name):
        now_date = str(self.commonUtils.get_us_today_time())
        month_ago_date = str(self.commonUtils.get_month_ago_date())
        stock_daily = self.commonStockService.select_stock_batch("us_stock_daily", stock_name, month_ago_date, now_date)

        return self.calculate_nearby_daily_status(stock_daily)

    def us_substock_trend(self, substock_exist_list):
        for symbol_name in substock_exist_list:
            if len(symbol_name) > 0:
                symbol_name_array = symbol_name.split("_")
                if len(symbol_name_array) >= 2 :
                    symbol = symbol_name_array[0]
                    name = symbol_name_array[1]
                    calculate_status = self.us_stock_trend(symbol)
                    if bool(calculate_status):
                        print('symbol', symbol, 'calculate_status', calculate_status, name)

    def us_all_stock_trend(self):
        print("------ 标普500指数 -------")
        sp500_substock_exist_list = self.get_stock_exist(6).split(",")
        self.us_substock_trend(sp500_substock_exist_list)
        print("")

        print("------ 道琼斯指数 -------")
        dowjones_substock_exist_list = self.get_stock_exist(8).split(",")
        self.us_substock_trend(dowjones_substock_exist_list)
        print("")

        print("------ 纳斯达克100指数 -------")
        nasdaq_substock_exist_list = self.get_stock_exist(7).split(",")
        self.us_substock_trend(nasdaq_substock_exist_list)
        print("")

        print("------ 采矿 -------")
        mining_substock_exist_list = self.get_stock_exist(31).split(",")
        self.us_substock_trend(mining_substock_exist_list)
        print("")

        print("------ 钢铁 -------")
        steel_substock_exist_list = self.get_stock_exist(32).split(",")
        self.us_substock_trend(steel_substock_exist_list)
        print("")

        print("------ 化学制品 -------")
        chemicals_substock_exist_list = self.get_stock_exist(33).split(",")
        self.us_substock_trend(chemicals_substock_exist_list)
        print("")

        print("------ 林产品/制纸 -------")
        papermaking_substock_exist_list = self.get_stock_exist(34).split(",")
        self.us_substock_trend(papermaking_substock_exist_list)
        print("")

        print("------ 计算机 -------")
        compute_substock_exist_list = self.get_stock_exist(35).split(",")
        self.us_substock_trend(compute_substock_exist_list)
        print("")

        print("------ 半导体 -------")
        semiconductor_substock_exist_list = self.get_stock_exist(36).split(",")
        self.us_substock_trend(semiconductor_substock_exist_list)
        print("")

        print("------ 软件 -------")
        software_substock_exist_list = self.get_stock_exist(37).split(",")
        self.us_substock_trend(software_substock_exist_list)
        print("")

        print("------ 办公/企业设备 -------")
        office_substock_exist_list = self.get_stock_exist(38).split(",")
        self.us_substock_trend(office_substock_exist_list)
        print("")

        print("------ 计算机硬件/企业设备 -------")
        hardware_substock_exist_list = self.get_stock_exist(39).split(",")
        self.us_substock_trend(hardware_substock_exist_list)
        print("")

        print("------ 电力组件与设备 -------")
        power_components_substock_exist_list = self.get_stock_exist(40).split(",")
        self.us_substock_trend(power_components_substock_exist_list)
        print("")

        print("------ 运输 -------")
        transport_substock_exist_list = self.get_stock_exist(41).split(",")
        self.us_substock_trend(transport_substock_exist_list)
        print("")

        print("------ 电子 -------")
        electronic_substock_exist_list = self.get_stock_exist(42).split(",")
        self.us_substock_trend(electronic_substock_exist_list)
        print("")

        print("------ 多元化制造商 -------")
        diversified_manufacturers_substock_exist_list = self.get_stock_exist(43).split(",")
        self.us_substock_trend(diversified_manufacturers_substock_exist_list)
        print("")

        print("------ 航空航天/国防 -------")
        aerospace_substock_exist_list = self.get_stock_exist(44).split(",")
        self.us_substock_trend(aerospace_substock_exist_list)
        print("")

        print("------ 包装容器 -------")
        packaging_substock_exist_list = self.get_stock_exist(45).split(",")
        self.us_substock_trend(packaging_substock_exist_list)
        print("")

        print("------ 建筑材料 -------")
        building_materials_substock_exist_list = self.get_stock_exist(46).split(",")
        self.us_substock_trend(building_materials_substock_exist_list)
        print("")

        print("------ 机械-建筑-矿业 -------")
        machinery_construction_mining_substock_exist_list = self.get_stock_exist(47).split(",")
        self.us_substock_trend(machinery_construction_mining_substock_exist_list)
        print("")

        print("------ 金属构件/部件 -------")
        metal_components_substock_exist_list = self.get_stock_exist(48).split(",")
        self.us_substock_trend(metal_components_substock_exist_list)
        print("")

        print("------ 工程建设 -------")
        construction_substock_exist_list = self.get_stock_exist(49).split(",")
        self.us_substock_trend(construction_substock_exist_list)
        print("")

        print("------ 机械多元 -------")
        mechanical_diversity_substock_exist_list = self.get_stock_exist(50).split(",")
        self.us_substock_trend(mechanical_diversity_substock_exist_list)
        print("")

        print("------ 环境控制 -------")
        environmental_control_substock_exist_list = self.get_stock_exist(51).split(",")
        self.us_substock_trend(environmental_control_substock_exist_list)
        print("")

        print("------ 手工/机器工具 -------")
        manual_machine_tools_substock_exist_list = self.get_stock_exist(52).split(",")
        self.us_substock_trend(manual_machine_tools_substock_exist_list)
        print("")

        print("------ 运输及出租 -------")
        transport_substock_exist_list = self.get_stock_exist(53).split(",")
        self.us_substock_trend(transport_substock_exist_list)
        print("")

        print("------ 造船 -------")
        shipbuilding_substock_exist_list = self.get_stock_exist(54).split(",")
        self.us_substock_trend(shipbuilding_substock_exist_list)
        print("")

        print("------ 制药 -------")
        pharmaceutical_substock_exist_list = self.get_stock_exist(55).split(",")
        self.us_substock_trend(pharmaceutical_substock_exist_list)
        print("")

        print("------ 商业服务 -------")
        business_service_substock_exist_list = self.get_stock_exist(56).split(",")
        self.us_substock_trend(business_service_substock_exist_list)
        print("")

        print("------ 食品 -------")
        food_substock_exist_list = self.get_stock_exist(57).split(",")
        self.us_substock_trend(food_substock_exist_list)
        print("")

        print("------ 生物技术 -------")
        biotechnology_substock_exist_list = self.get_stock_exist(58).split(",")
        self.us_substock_trend(biotechnology_substock_exist_list)
        print("")

        print("------ 化妆品/护理 -------")
        cosmetics_nursing_substock_exist_list = self.get_stock_exist(59).split(",")
        self.us_substock_trend(cosmetics_nursing_substock_exist_list)
        print("")

        print("------ 医疗保健产品 -------")
        healthcare_products_substock_exist_list = self.get_stock_exist(60).split(",")
        self.us_substock_trend(healthcare_products_substock_exist_list)
        print("")

        print("------ 饮料 -------")
        drinks_substock_exist_list = self.get_stock_exist(61).split(",")
        self.us_substock_trend(drinks_substock_exist_list)
        print("")

        print("------ 健康护理服务 -------")
        health_care_services_substock_exist_list = self.get_stock_exist(62).split(",")
        self.us_substock_trend(health_care_services_substock_exist_list)
        print("")

        print("------ 农业 -------")
        agriculture_substock_exist_list = self.get_stock_exist(63).split(",")
        self.us_substock_trend(agriculture_substock_exist_list)
        print("")

        print("------ 家庭产品/用品 -------")
        household_products_substock_exist_list = self.get_stock_exist(64).split(",")
        self.us_substock_trend(household_products_substock_exist_list)
        print("")

        print("------ 电力 -------")
        electricity_substock_exist_list = self.get_stock_exist(65).split(",")
        self.us_substock_trend(electricity_substock_exist_list)
        print("")

        print("------ 水业 -------")
        water_industry_substock_exist_list = self.get_stock_exist(66).split(",")
        self.us_substock_trend(water_industry_substock_exist_list)
        print("")

        print("------ 天然气 -------")
        natural_gas_substock_exist_list = self.get_stock_exist(67).split(",")
        self.us_substock_trend(natural_gas_substock_exist_list)
        print("")

        print("------ 保险 -------")
        insurance_substock_exist_list = self.get_stock_exist(68).split(",")
        self.us_substock_trend(insurance_substock_exist_list)
        print("")

        print("------ 多元化金融服务 -------")
        diversified_financial_services_substock_exist_list = self.get_stock_exist(69).split(",")
        self.us_substock_trend(diversified_financial_services_substock_exist_list)
        print("")

        print("------ 银行 -------")
        bank_substock_exist_list = self.get_stock_exist(70).split(",")
        self.us_substock_trend(bank_substock_exist_list)
        print("")

        print("------ 房地产 -------")
        real_estate_substock_exist_list = self.get_stock_exist(71).split(",")
        self.us_substock_trend(real_estate_substock_exist_list)
        print("")

        print("------ 房地产信托投资基金 -------")
        real_estate_investment_trust_substock_exist_list = self.get_stock_exist(72).split(",")
        self.us_substock_trend(real_estate_investment_trust_substock_exist_list)
        print("")

        # print("------ 私募股权投资 -------")
        # private_equity_investment_substock_exist_list = self.get_stock_exist(73).split(",")
        # self.us_substock_trend(private_equity_investment_substock_exist_list)
        # print("")

        # print("------ 储蓄及贷款 -------")
        # savings_and_loans_substock_exist_list = self.get_stock_exist(74).split(",")
        # self.us_substock_trend(savings_and_loans_substock_exist_list)
        # print("")

        # print("------ 投资公司 -------")
        # investment_company_substock_exist_list = self.get_stock_exist(75).split(",")
        # self.us_substock_trend(investment_company_substock_exist_list)
        # print("")

        print("------ 电信 -------")
        telecommunications_substock_exist_list = self.get_stock_exist(76).split(",")
        self.us_substock_trend(telecommunications_substock_exist_list)
        print("")

        print("------ 广告 -------")
        advertising_substock_exist_list = self.get_stock_exist(77).split(",")
        self.us_substock_trend(advertising_substock_exist_list)
        print("")

        print("------ 互联网 -------")
        internet_substock_exist_list = self.get_stock_exist(78).split(",")
        self.us_substock_trend(internet_substock_exist_list)
        print("")

        print("------ 媒体 -------")
        media_substock_exist_list = self.get_stock_exist(79).split(",")
        self.us_substock_trend(media_substock_exist_list)
        print("")

        print("------ 媒体内容 -------")
        media_content_substock_exist_list = self.get_stock_exist(80).split(",")
        self.us_substock_trend(media_content_substock_exist_list)
        print("")

        print("------ 零售 -------")
        retail_substock_exist_list = self.get_stock_exist(81).split(",")
        self.us_substock_trend(retail_substock_exist_list)
        print("")

        print("------ 娱乐 -------")
        entertainment_substock_exist_list = self.get_stock_exist(82).split(",")
        self.us_substock_trend(entertainment_substock_exist_list)
        print("")

        print("------ 汽车部件与设备 -------")
        cart_parts_and_equipment_substock_exist_list = self.get_stock_exist(83).split(",")
        self.us_substock_trend(cart_parts_and_equipment_substock_exist_list)
        print("")

        print("------ 航空公司 -------")
        airline_substock_exist_list = self.get_stock_exist(84).split(",")
        self.us_substock_trend(airline_substock_exist_list)
        print("")

        print("------ 房屋建造商 -------")
        house_builder_substock_exist_list = self.get_stock_exist(85).split(",")
        self.us_substock_trend(house_builder_substock_exist_list)
        print("")

        print("------ 家具家饰 -------")
        furniture_furnishings_substock_exist_list = self.get_stock_exist(86).split(",")
        self.us_substock_trend(furniture_furnishings_substock_exist_list)
        print("")

        print("------ 服饰 -------")
        clothes_substock_exist_list = self.get_stock_exist(87).split(",")
        self.us_substock_trend(clothes_substock_exist_list)
        print("")

        print("------ 汽车制造 -------")
        car_manufacturer_substock_exist_list = self.get_stock_exist(88).split(",")
        self.us_substock_trend(car_manufacturer_substock_exist_list)
        print("")

        print("------ 住宿 -------")
        stay_substock_exist_list = self.get_stock_exist(89).split(",")
        self.us_substock_trend(stay_substock_exist_list)
        print("")

        print("------ 休闲 -------")
        casual_substock_exist_list = self.get_stock_exist(90).split(",")
        self.us_substock_trend(casual_substock_exist_list)
        print("")

        print("------ 销售/批发 -------")
        sales_wholesale_substock_exist_list = self.get_stock_exist(91).split(",")
        self.us_substock_trend(sales_wholesale_substock_exist_list)
        print("")

        print("------ 纺织品 -------")
        textile_substock_exist_list = self.get_stock_exist(92).split(",")
        self.us_substock_trend(textile_substock_exist_list)
        print("")

        print("------ 玩具/游戏/爱好 -------")
        toys_games_hobbies_substock_exist_list = self.get_stock_exist(93).split(",")
        self.us_substock_trend(toys_games_hobbies_substock_exist_list)
        print("")

        print("------ 办公家具 -------")
        office_furniture_substock_exist_list = self.get_stock_exist(94).split(",")
        self.us_substock_trend(office_furniture_substock_exist_list)
        print("")

        print("------ 家用器具 -------")
        household_appliances_substock_exist_list = self.get_stock_exist(95).split(",")
        self.us_substock_trend(household_appliances_substock_exist_list)
        print("")

        print("------ 存储/仓储 -------")
        storage_warehouse_substock_exist_list = self.get_stock_exist(96).split(",")
        self.us_substock_trend(storage_warehouse_substock_exist_list)
        print("")

        print("------ 油气服务 -------")
        oil_and_gas_service_substock_exist_list = self.get_stock_exist(97).split(",")
        self.us_substock_trend(oil_and_gas_service_substock_exist_list)
        print("")

        print("------ 油气 -------")
        oil_and_gas_substock_exist_list = self.get_stock_exist(98).split(",")
        self.us_substock_trend(oil_and_gas_substock_exist_list)
        print("")

        print("------ 能源-替代能源 -------")
        alternative_energy_substock_exist_list = self.get_stock_exist(99).split(",")
        self.us_substock_trend(alternative_energy_substock_exist_list)
        print("")

        print("------ 管道 -------")
        pipeline_substock_exist_list = self.get_stock_exist(100).split(",")
        self.us_substock_trend(pipeline_substock_exist_list)
        print("")

        print("------ 煤炭 -------")
        coal_substock_exist_list = self.get_stock_exist(101).split(",")
        self.us_substock_trend(coal_substock_exist_list)
        print("")

        print("------ 中概股 -------")
        china_concept_substock_exist_list = self.get_stock_exist(102).split(",")
        self.us_substock_trend(china_concept_substock_exist_list)
        print("")

        print("------ 其它 -------")
        other_substock_exist_list = self.get_stock_exist(103).split(",")
        self.us_substock_trend(other_substock_exist_list)
        print("")

if __name__ == '__main__':
    st = StockTrend()
    #st.stock_trend("00700")
    #st.hk_all_stock_trend()
    st.us_all_stock_trend()
