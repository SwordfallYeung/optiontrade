from com.swordfall.trade.common.CommonIndexesDaily import CommonIndexesDaily
from datetime import datetime
import pandas as pd
import requests
from com.swordfall.service.us.UStockService import UStockService
import json,re

class UsIndexesDaily:

    def __init__(self):
        self.common_indexes_daily = CommonIndexesDaily()
        self.us_stock_service = UStockService()

    def get_us_indexes_daily(self, index_name, start_date, end_date):
        '''
        获取美股道琼斯指数、标普500指数、纳斯达克综合指数指定日期内的每天行情
        :param start_date: 开始日期
        :param end_date: 结束日期
        :return:
        '''
        start_time = datetime.now()
        print("get_us_indexes_daily 获取美股三大指数指定日期内的每天行情 start_time:", start_time)

        self.common_indexes_daily.get_index_daily(country="美国", index_name=index_name, start_date=start_date,
                                             end_date=end_date,
                                             method_name="get_us_indexes_daily" + "_" + index_name)

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_us_indexes_daily 获取美股三大指数指定日期内的每天行情 end_time:", end_time, "耗时:", time)

    def update_us_index_daily_lastest(self, index_name):
        '''
        更新美股指数最新行情
        :return:
        '''
        #start_time = datetime.now()
        #print("update_us_index_daily_lastest 更新美股指数最新行情 start_time:", start_time)

        self.common_indexes_daily.update_index_daily_lastest(country="美国", index_name=index_name,
                                                        method_name="update_us_index_daily_lastest")
        #end_time = datetime.now()
        #time = (end_time - start_time)
        #print("update_us_index_daily_lastest 每天更新美股三大指数行情 end_time:", end_time, "耗时:", time)

    def update_us_three_indexes_daily_lastest(self):
        '''
        更新美股美股道琼斯指数、标普500指数、纳斯达克综合指数最新行情
        :return:
        '''
        start_time = datetime.now()
        print("update_us_three_indexes_daily_lastest 每天更新美股三大指数行情 start_time:", start_time)

        self.update_us_index_daily_lastest("道琼斯指数")
        self.update_us_index_daily_lastest("标普500指数")
        self.update_us_index_daily_lastest("纳斯达克综合指数")

        end_time = datetime.now()
        time = (end_time - start_time)
        print("update_us_three_indexes_daily_lastest 每天更新美股三大指数行情 end_time:", end_time, "耗时:", time)

    def get_us_indexes_daily_substock_deprecated(self, url, id, type):
        start_time = datetime.now()
        print("get_us_indexes_daily_substock_deprecated start_time:", start_time)

        # https://www.slickcharts.com/sp500
        # https://www.slickcharts.com/nasdaq100
        # https://www.slickcharts.com/dowjones

        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

        request = requests.get(url, headers=headers)
        data = pd.read_html(request.text)[0]

        # 欄位『Symbol』就是股票代碼
        sub_stocks_list = data.Symbol.values

        index_substock_exist = ""

        for symbol_name in sub_stocks_list:
            index_substock_exist += symbol_name + ","

        self.update_us_index_substock_list_exist(id, index_substock_exist, type, len(sub_stocks_list))

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_us_indexes_daily_substock_deprecated end_time:", end_time, "耗时:", time)

    def parsing_us_indexes_substock(self, salt, id):
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

        mktcap = 20000000000
        page = 1
        flag = True
        n = 0
        substock_exist = ""
        i = 0

        while(flag):
            url = "http://stock.finance.sina.com.cn/usstock/api/jsonp.php/IO.XSRV2.CallbackList['" + salt + "']/US_CategoryService.getChengfen?page=" + str(page) + "&num=60&sort=mktcap&asc=0&market=&id=&type=" + id
            request = requests.get(url, headers=headers)
            request_content = re.sub(r'IO.XSRV2.CallbackList.*]\(', "",
                                     request.text.replace("/*<script>location.href='//sina.com';</script>*/\n", "").replace(");", ""))
            js = json.loads(request_content)

            count = int(js['count']['up']) + int(js['count']['down']) + int(js['count']['z'])
            n += len(js['data'])

            if salt == "Zh5NOtRXXXZ5ZRHU":
                for stock in js['data']:
                    if int(float(stock['mktcap'])) >= mktcap:
                        symbol_name = stock['symbol'] + "_" + stock['cname'].replace(",", "")
                        substock_exist += symbol_name + ","
                        i += 1
                    else:
                        flag = False
                        break
            else:
                for stock in js['data']:
                    symbol_name = stock['symbol'] + "_" + stock['cname'].replace(",", "")
                    substock_exist += symbol_name + ","
                    i += 1
            if count == n:
                flag = False

            page += 1

        return (i, substock_exist)

    def get_us_indexes_daily_substock(self):
        start_time = datetime.now()
        print("get_us_indexes_daily_substock start_time:", start_time)

        print("------ 标普500 -------")
        (sp500_count, sp500_data) = self.parsing_us_indexes_substock('UF1rlz5CGEXBXJu1', '2')
        self.update_us_index_substock_list_exist(6, sp500_data, 'us_plate_sp500_substock_list', sp500_count)

        print("------ 纳克达斯 -------")
        (nasdaq_count, nasdaq_data) = self.parsing_us_indexes_substock('Zh5NOtRXXXZ5ZRHU', '1')
        self.update_us_index_substock_list_exist(7, nasdaq_data, 'us_plate_nasdaq_substock_list', nasdaq_count)

        print("------ 道琼斯 -------")
        (dowjones_count, dowjones_data) = self.parsing_us_indexes_substock('UF1rlz5CGEXAXJu1', '3')
        self.update_us_index_substock_list_exist(8, dowjones_data, 'us_plate_dowjones_substock_list', dowjones_count)

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_us_indexes_daily_substock end_time:", end_time, "耗时:", time)

    def parsing_us_plate_substock(self, salt, id, mktcap):
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

        #mktcap = 10000000000
        page = 1
        flag = True
        n = 0
        substock_exist = ""
        i = 0

        while(flag):
            url = "http://stock.finance.sina.com.cn/usstock/api/jsonp.php/IO.XSRV2.CallbackList['" + salt + "']/US_CategoryService.getList?page=" + str(page) + "&num=60&sort=&asc=0&market=&id=" + id
            request = requests.get(url, headers=headers)
            request_content = re.sub(r'IO.XSRV2.CallbackList.*]\(', "",
                                     request.text.replace("/*<script>location.href='//sina.com';</script>*/\n", "").replace(");", ""))
            js = json.loads(request_content)

            count = js['count']
            n += len(js['data'])

            for stock in js['data']:
                if int(stock['mktcap']) >= mktcap:
                    symbol_name = stock['symbol'] + "_" + stock['cname'].replace(",", "")
                    substock_exist += symbol_name + ","
                    i += 1
                else:
                    flag = False
                    break
            if int(count) == n:
                flag = False

            page += 1

        return (i, substock_exist)

    def get_us_plate_substock(self):
        start_time = datetime.now()
        print("get_us_plate_substock start_time:", start_time)

        print("------ 采矿 -------")
        (mining_count, mining_data) = self.parsing_us_plate_substock('0BGdPLKaSOnAYUKL', '2', 10000000000)
        self.update_us_index_substock_list_exist(31, mining_data, 'us_plate_mining_substock_list',  mining_count)

        print("------ 钢铁 -------")
        (steel_count, steel_data) = self.parsing_us_plate_substock('QRhIHyKEpcO0MInd', '46', 13000000000)
        self.update_us_index_substock_list_exist(32, steel_data, 'us_plate_steel_substock_list', steel_count)

        print("------ 化学制品 -------")
        (chemicals_count, chemicals_data) = self.parsing_us_plate_substock('8Wp$XMIlfTVJcCHy', '88', 30000000000)
        self.update_us_index_substock_list_exist(33, chemicals_data, 'us_plate_chemicals_substock_list', chemicals_count)

        # print("------ 林产品/制纸 -------")
        # (papermaking_count, papermaking_data) = self.parsing_us_plate_substock('f0j3lgvpbae1Fo4p', '180')
        # self.update_us_index_substock_list_exist(34, papermaking_data, 'us_plate_papermaking_substock_list', papermaking_count)

        print("------ 计算机 -------")
        (compute_count, compute_data) = self.parsing_us_plate_substock('ilPtHiClt_p8HArD', '5', 26000000000)
        self.update_us_index_substock_list_exist(35, compute_data, 'us_plate_compute_substock_list', compute_count)

        print("------ 半导体 -------")
        (semiconductor_count, semiconductor_data) = self.parsing_us_plate_substock('uAZnIudtFy7PjpOt', '12', 20000000000)
        self.update_us_index_substock_list_exist(36, semiconductor_data, 'us_plate_semiconductor_substock_list', semiconductor_count)

        print("------ 软件 -------")
        (software_count, software_data) = self.parsing_us_plate_substock('TvDHcqIaIf98HArD', '14', 18000000000)
        self.update_us_index_substock_list_exist(37, software_data, 'us_plate_software_substock_list', software_count)

        # print("------ 办公/企业设备 -------")
        # (office_count, office_data) = self.parsing_us_plate_substock('O0j3lgC$G0lPFo4p', '642')
        # self.update_us_index_substock_list_exist(38, office_data, 'us_plate_office_substock_list', office_count)

        print("------ 计算机硬件/企业设备 -------")
        (hardware_count, hardware_data) = self.parsing_us_plate_substock('8Wp$XMoQpRW4cCHy', '681', 20000000000)
        self.update_us_index_substock_list_exist(39, hardware_data, 'us_plate_hardware_substock_list', hardware_count)

        print("------ 电力组件与设备 -------")
        (power_components_count, power_components_data) = self.parsing_us_plate_substock('tnuEDFReoimdDZGk', '7', 20000000000)
        self.update_us_index_substock_list_exist(40, power_components_data, 'us_plate_power_components_substock_list', power_components_count)

        import time
        time.sleep(2)

        print("------ 运输 -------")
        (transport_count, transport_data) = self.parsing_us_plate_substock('B4FC3grlt_p8HArD', '34', 100000000000)
        self.update_us_index_substock_list_exist(41, transport_data, 'us_plate_transport_substock_list', transport_count)

        print("------ 电子 -------")
        (electronic_count, electronic_data) = self.parsing_us_plate_substock('8Wp$XMIifTVJcCHy', '49', 30000000000)
        self.update_us_index_substock_list_exist(42, electronic_data, 'us_plate_electronic_substock_list', electronic_count)

        print("------ 多元化制造商 -------")
        (diversified_manufacturers_count, diversified_manufacturers_data) = self.parsing_us_plate_substock('CvDHcqNHIf98HArD', '58', 30000000000)
        self.update_us_index_substock_list_exist(43, diversified_manufacturers_data, 'us_plate_diversified_manufacturers_substock_list', diversified_manufacturers_count)

        print("------ 航空航天/国防 -------")
        (aerospace_count, aerospace_data) = self.parsing_us_plate_substock('nHH$Ii0iEx6NC5Ap', '60', 50000000000)
        self.update_us_index_substock_list_exist(44, aerospace_data, 'us_plate_aerospace_substock_list', aerospace_count)

        print("------ 包装容器 -------")
        (packaging_count, packaging_data) = self.parsing_us_plate_substock('az83lL34XmFyuF_K', '65', 5000000000)
        self.update_us_index_substock_list_exist(45, packaging_data, 'us_plate_packaging_substock_list', packaging_count)

        # print("------ 建筑材料 -------")
        # (building_materials_count, building_materials_data) = self.parsing_us_plate_substock('CvDHcqYGIf98HArD', '86')
        # self.update_us_index_substock_list_exist(46, building_materials_data, 'us_plate_building_materials_substock_list', building_materials_count)

        # print("------ 机械-建筑-矿业 -------")
        # (machinery_construction_mining_count, machinery_construction_mining_data) = self.parsing_us_plate_substock('FF3AiCNuoimdDZGk', '90')
        # self.update_us_index_substock_list_exist(47, machinery_construction_mining_data, 'us_plate_machinery_construction_mining_substock_list', machinery_construction_mining_count)

        # print("------ 金属构件/部件 -------")
        # (metal_components_count, metal_components_data) = self.parsing_us_plate_substock('cgntpUSoWa58GJY3', '101')
        # self.update_us_index_substock_list_exist(48, metal_components_data, 'us_plate_metal_components_substock_list', metal_components_count)

        # print("------ 工程建设 -------")
        # (construction_count, construction_data) = self.parsing_us_plate_substock('cgntpUSvi0t8GJY3', '117')
        # self.update_us_index_substock_list_exist(49, construction_data, 'us_plate_construction_substock_list', construction_count)

        # print("------ 机械多元 -------")
        # (mechanical_diversity_count, mechanical_diversity_data) = self.parsing_us_plate_substock('CvDHcqLfQE_THArD', '134')
        # self.update_us_index_substock_list_exist(50, mechanical_diversity_data, 'us_plate_mechanical_diversity_substock_list', mechanical_diversity_count)

        time.sleep(2)

        # print("------ 环境控制 -------")
        # (environmental_control_count, environmental_control_data) = self.parsing_us_plate_substock('6MizKiL$yyZMC5Ap', '141')
        # self.update_us_index_substock_list_exist(51, environmental_control_data, 'us_plate_environmental_control_substock_list', environmental_control_count)

        # print("------ 手工/机器工具 -------")
        # (manual_machine_tools_count, manual_machine_tools_data) = self.parsing_us_plate_substock('J0j3lgS312LpFo4p', '357')
        # self.update_us_index_substock_list_exist(52, manual_machine_tools_data, 'us_plate_manual_machine_tools_substock_list', manual_machine_tools_count)

        # print("------ 运输及出租 -------")
        # (transport_and_rental_count, transport_and_rental_data) = self.parsing_us_plate_substock('O0j3lgSuW_3qFo4p', '336')
        # self.update_us_index_substock_list_exist(53, transport_and_rental_data, 'us_plate_transport_and_rental_substock_list', transport_and_rental_count)

        # print("------ 造船 -------")
        # (shipbuilding_count, shipbuilding_data) = self.parsing_us_plate_substock('tw7ZFdS$IeK4Fo4p', '615')
        # self.update_us_index_substock_list_exist(54, shipbuilding_data, 'us_plate_shipbuilding_substock_list', shipbuilding_count)

        print("------ 制药 -------")
        (pharmaceutical_count, pharmaceutical_data) = self.parsing_us_plate_substock('FF3AiCNuoimdDZGk', '10', 100000000000)
        self.update_us_index_substock_list_exist(55, pharmaceutical_data, 'us_plate_pharmaceutical_substock_list', pharmaceutical_count)

        print("------ 商业服务 -------")
        (business_service_count, business_service_data) = self.parsing_us_plate_substock('JyRdhgLht_p8HArD', '16', 20000000000)
        self.update_us_index_substock_list_exist(56, business_service_data, 'us_plate_business_service_substock_list', business_service_count)

        print("------ 食品 -------")
        (food_count, food_data) = self.parsing_us_plate_substock('CvDHcqNHIf98HArD', '18', 20000000000)
        self.update_us_index_substock_list_exist(57, food_data, 'us_plate_food_substock_list', food_count)

        print("------ 生物技术 -------")
        (biotechnology_count, biotechnology_data) = self.parsing_us_plate_substock('wdv5LWh7fBt9Rqml', '39', 50000000000)
        self.update_us_index_substock_list_exist(58, biotechnology_data, 'us_plate_biotechnology_substock_list', biotechnology_count)

        print("------ 化妆品/护理 -------")
        (cosmetics_nursing_count, cosmetics_nursing_data) = self.parsing_us_plate_substock('TvDHcqIaIf98HArD', '54', 50000000000)
        self.update_us_index_substock_list_exist(59, cosmetics_nursing_data, 'us_plate_cosmetics_nursing_substock_list', cosmetics_nursing_count)

        print("------ 医疗保健产品 -------")
        (healthcare_products_count, healthcare_products_data) = self.parsing_us_plate_substock('cgntpUixS198GJY3', '63', 50000000000)
        self.update_us_index_substock_list_exist(60, healthcare_products_data, 'us_plate_healthcare_products_substock_list', healthcare_products_count)

        time.sleep(2)

        print("------ 饮料 -------")
        (drinks_count, drinks_data) = self.parsing_us_plate_substock('B4FC3grlt_p8HArD', '74', 100000000000)
        self.update_us_index_substock_list_exist(61, drinks_data, 'us_plate_drinks_substock_list', drinks_count)

        print("------ 健康护理服务 -------")
        (health_care_services_count, health_care_services_data) = self.parsing_us_plate_substock('TvDHcqIBIf98HArD', '95', 10000000000)
        self.update_us_index_substock_list_exist(62, health_care_services_data, 'us_plate_health_care_services_substock_list', health_care_services_count)

        print("------ 农业 -------")
        (agriculture_count, agriculture_data) = self.parsing_us_plate_substock('x_p$WQthguXxK5ae', '159', 80000000000)
        self.update_us_index_substock_list_exist(63, agriculture_data, 'us_plate_agriculture_substock_list', agriculture_count)

        # print("------ 家庭产品/用品 -------")
        # (household_products_count, household_products_data) = self.parsing_us_plate_substock('8Wp$XMoQpRW4cCHy', '283')
        # self.update_us_index_substock_list_exist(64, household_products_data, 'us_plate_household_products_substock_list', household_products_count)

        print("------ 电力 -------")
        (electricity_count, electricity_data) = self.parsing_us_plate_substock('nHH$Ii09Ex6NC5Ap', '21', 37000000000)
        self.update_us_index_substock_list_exist(65, electricity_data, 'us_plate_electricity_substock_list',electricity_count)

        # print("------ 水业 -------")
        # (water_industry_count, water_industry_data) = self.parsing_us_plate_substock('J0j3lgC$G0lPFo4p', '272')
        # self.update_us_index_substock_list_exist(66, water_industry_data, 'us_plate_water_industry_substock_list', water_industry_count)

        # print("------ 天然气 -------")
        # (natural_gas_count, natural_gas_data) = self.parsing_us_plate_substock('tw7ZFdCags52Fo4p', '334')
        # self.update_us_index_substock_list_exist(67, natural_gas_data, 'us_plate_natural_gas_substock_list', natural_gas_count)

        # print("------ 保险 -------")
        # (insurance_count, insurance_data) = self.parsing_us_plate_substock('az83lL34XmFyuF_K', '25')
        # self.update_us_index_substock_list_exist(68, insurance_data, 'us_plate_insurance_substock_list', insurance_count)

        print("------ 多元化金融服务 -------")
        (diversified_financial_services_count, diversified_financial_services_data) = self.parsing_us_plate_substock('JyRdhgLht_p8HArD', '56', 45000000000)
        self.update_us_index_substock_list_exist(69, diversified_financial_services_data, 'us_plate_diversified_financial_services_substock_list', diversified_financial_services_count)

        print("------ 银行 -------")
        (bank_count, bank_data) = self.parsing_us_plate_substock('nHH$Ii09Ex6NC5Ap', '61', 55000000000)
        self.update_us_index_substock_list_exist(70, bank_data, 'us_plate_bank_substock_list', bank_count)

        time.sleep(2)

        # print("------ 房地产 -------")
        # (real_estate_count, real_estate_data) = self.parsing_us_plate_substock('CvDHcqLffcT9HArD', '131')
        # self.update_us_index_substock_list_exist(71, real_estate_data, 'us_plate_real_estate_substock_list', real_estate_count)

        # print("------ 房地产信托投资基金 -------")
        # (real_estate_investment_trust_count, real_estate_investment_trust_data) = self.parsing_us_plate_substock('O0j3lgNwcypDFo4p', '227')
        # self.update_us_index_substock_list_exist(72, real_estate_investment_trust_data, 'us_plate_real_estate_investment_trust_substock_list', real_estate_investment_trust_count)

        # print("------ 私募股权投资 -------")
        # (private_equity_investment_count, private_equity_investment_data) = self.parsing_us_plate_substock('O0j3lgC$G0lPFo4p', '240')
        # self.update_us_index_substock_list_exist(73, private_equity_investment_data, 'us_plate_private_equity_investment_substock_list', private_equity_investment_count)

        # print("------ 储蓄及贷款 -------")
        # (savings_and_loans_count, savings_and_loans_data) = self.parsing_us_plate_substock('O0j3lgC$G0lPFo4p', '242')
        # self.update_us_index_substock_list_exist(74, savings_and_loans_data, 'us_plate_savings_and_loans_substock_list', savings_and_loans_count)

        # print("------ 投资公司 -------")
        # (investment_company_count, investment_company_data) = self.parsing_us_plate_substock('J0j3lgC$G0lPFo4p', '261')
        # self.update_us_index_substock_list_exist(75, investment_company_data, 'us_plate_investment_company_substock_list', investment_company_count)

        print("------ 电信 -------")
        (telecommunications_count, telecommunications_data) = self.parsing_us_plate_substock('cgntpUyzS198GJY3', '30', 23000000000)
        self.update_us_index_substock_list_exist(76, telecommunications_data, 'us_plate_telecommunications_substock_list', telecommunications_count)

        # print("------ 广告 -------")
        # (advertising_count, advertising_data) = self.parsing_us_plate_substock('az83lL3lXmFyuF_K', '36')
        # self.update_us_index_substock_list_exist(77, advertising_data, 'us_plate_advertising_substock_list', advertising_count)

        print("------ 互联网 -------")
        (internet_count, internet_data) = self.parsing_us_plate_substock('EF3AiCaooimdDZGk', '41', 30000000000)
        self.update_us_index_substock_list_exist(78, internet_data, 'us_plate_internet_substock_list', internet_count)

        print("------ 媒体 -------")
        (media_count, media_data) = self.parsing_us_plate_substock('wdv5LWh7fBt9Rqml', '79', 100000000000)
        self.update_us_index_substock_list_exist(79, media_data, 'us_plate_media_substock_list', media_count)

        print("------ 媒体内容 -------")
        (media_content_count, media_content_data) = self.parsing_us_plate_substock('O0j3lgdVFfrHFo4p', '702', 30000000000)
        self.update_us_index_substock_list_exist(80, media_content_data, 'us_plate_media_content_substock_list', media_content_count)

        time.sleep(2)

        print("------ 零售 -------")
        (retail_count, retail_data) = self.parsing_us_plate_substock('uAZnIudtFy7PjpOt', '52', 20000000000)
        self.update_us_index_substock_list_exist(81, retail_data, 'us_plate_retail_substock_list', retail_count)

        # print("------ 娱乐 -------")
        # (entertainment_count, entertainment_data) = self.parsing_us_plate_substock('nHH$IikJEx6NC5Ap', '72')
        # self.update_us_index_substock_list_exist(82, entertainment_data, 'us_plate_entertainment_substock_list', entertainment_count)

        # print("------ 汽车部件与设备 -------")
        # (cart_parts_and_equipment_count, cart_parts_and_equipment_data) = self.parsing_us_plate_substock('8Wp$XMJpfTVJcCHy', '84')
        # self.update_us_index_substock_list_exist(83, cart_parts_and_equipment_data, 'us_plate_cart_parts_and_equipment_substock_list', cart_parts_and_equipment_count)

        print("------ 航空公司 -------")
        (airline_count, airline_data) = self.parsing_us_plate_substock('cgntpUSoWa58GJY3', '103', 0)
        self.update_us_index_substock_list_exist(84, airline_data, 'us_plate_airline_substock_list', airline_count)

        print("------ 房屋建造商 -------")
        (house_builder_count, house_builder_data) = self.parsing_us_plate_substock('cgntpUSv9JTQGJY3', '110', 20000000000)
        self.update_us_index_substock_list_exist(85, house_builder_data, 'us_plate_house_builder_substock_list', house_builder_count)

        # print("------ 家具家饰 -------")
        # (furniture_furnishings_count, furniture_furnishings_data) = self.parsing_us_plate_substock('ilPtHiGw4BCfHArD', '139', 10000000000)
        # self.update_us_index_substock_list_exist(86, furniture_furnishings_data, 'us_plate_furniture_furnishings_substock_list', furniture_furnishings_count)

        # print("------ 服饰 -------")
        # (clothes_count, clothes_data) = self.parsing_us_plate_substock('x_p$WQtmbE9iK5ae', '148', 10000000000)
        # self.update_us_index_substock_list_exist(87, clothes_data, 'us_plate_clothes_substock_list', clothes_count)

        print("------ 汽车制造 -------")
        (car_manufacturer_count, car_manufacturer_data) = self.parsing_us_plate_substock('6MizKiL4$yTAC5Ap', '155', 20000000000)
        self.update_us_index_substock_list_exist(88, car_manufacturer_data, 'us_plate_car_manufacturer_substock_list', car_manufacturer_count)

        print("------ 住宿 -------")
        (stay_count, stay_data) = self.parsing_us_plate_substock('K4FC3gL_V9t8HArD', '176', 8000000000)
        self.update_us_index_substock_list_exist(89, stay_data, 'us_plate_stay_substock_list', stay_count)

        print("------ 休闲 -------")
        (casual_count, casual_data) = self.parsing_us_plate_substock('O0j3lgNwDBYSFo4p', '222', 4500000000)
        self.update_us_index_substock_list_exist(90, casual_data, 'us_plate_casual_substock_list', casual_count)

        time.sleep(2)

        # print("------ 销售/批发 -------")
        # (sales_wholesale_count, sales_wholesale_data) = self.parsing_us_plate_substock('O0j3lgC$FqXbFo4p', '256', 10000000000)
        # self.update_us_index_substock_list_exist(91, sales_wholesale_data, 'us_plate_sales_wholesale_substock_list', sales_wholesale_count)

        # print("------ 纺织品 -------")
        # (textile_count, textile_data) = self.parsing_us_plate_substock('yjD5LWn3nCEwRqml', '319', 10000000000)
        # self.update_us_index_substock_list_exist(92, textile_data, 'us_plate_textile_substock_list', textile_count)

        # print("------ 玩具/游戏/爱好 -------")
        # (toys_games_hobbies_count, toys_games_hobbies_data) = self.parsing_us_plate_substock('Ny93lgS1Bhf4Fo4p', '378')
        # self.update_us_index_substock_list_exist(93, toys_games_hobbies_data, 'us_plate_toys_games_hobbies_substock_list', toys_games_hobbies_count)

        # print("------ 办公家具 -------")
        # (office_furniture_count, office_furniture_data) = self.parsing_us_plate_substock('J0j3lgPBLCqFFo4p', '388')
        # self.update_us_index_substock_list_exist(94, office_furniture_data, 'us_plate_office_furniture_substock_list', office_furniture_count)

        # print("------ 家用器具 -------")
        # (household_appliances_count, household_appliances_data) = self.parsing_us_plate_substock('J0j3lgPGacdOFo4p', '398')
        # self.update_us_index_substock_list_exist(95, household_appliances_data, 'us_plate_household_appliances_substock_list', household_appliances_count)

        # print("------ 存储/仓储 -------")
        # (storage_warehouse_count, storage_warehouse_data) = self.parsing_us_plate_substock('J0j3lgtkYvs2Fo4p', '406')
        # self.update_us_index_substock_list_exist(96, storage_warehouse_data, 'us_plate_storage_warehouse_substock_list', storage_warehouse_count)

        print("------ 油气服务 -------")
        (oil_and_gas_service_count, oil_and_gas_service_data) = self.parsing_us_plate_substock('SGJ4pB4buMz9JptU', '68', 10000000000)
        self.update_us_index_substock_list_exist(97, oil_and_gas_service_data, 'us_plate_oil_and_gas_service_substock_list', oil_and_gas_service_count)

        print("------ 油气 -------")
        (oil_and_gas_count, oil_and_gas_data) = self.parsing_us_plate_substock('az83lL3lXmFyuF_K', '76', 20000000000)
        self.update_us_index_substock_list_exist(98, oil_and_gas_data, 'us_plate_oil_and_gas_substock_list', oil_and_gas_count)

        print("------ 能源-替代能源 -------")
        (alternative_energy_count, alternative_energy_data) = self.parsing_us_plate_substock('tw7ZFdi4iNBJFo4p', '109', 600000000)
        self.update_us_index_substock_list_exist(99, alternative_energy_data, 'us_plate_alternative_energy_substock_list', alternative_energy_count)

        print("------ 管道 -------")
        (pipeline_count, pipeline_data) = self.parsing_us_plate_substock('cgntpUSv9JTQGJY3', '112', 60000000000)
        self.update_us_index_substock_list_exist(100, pipeline_data, 'us_plate_pipeline_substock_list', pipeline_count)

        # print("------ 煤炭 -------")
        # (coal_count, coal_data) = self.parsing_us_plate_substock('tw7ZFdS$PtW_Fo4p', '210', 10000000000)
        # self.update_us_index_substock_list_exist(101, coal_data, 'us_plate_coal_substock_list', coal_count)

        end_time = datetime.now()
        time = (end_time - start_time)
        print("get_us_plate_substock end_time:", end_time, "耗时:", time)

    def get_us_plate_china_concept_stock(self):
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

        market_cap = 2000000000
        page = 1
        flag = True
        n = 0
        substock_exist = ""
        i = 0

        num_url = "http://money.finance.sina.com.cn/q/api/jsonp_v2.php/IO.XSRV2.CallbackList['177ygpkIfsyUHcjR']/US_ChinaStockService.getTotalNum?page=1&num=60&sort=&asc=0&market=&concept=0"
        request_num = requests.get(num_url, headers=headers)
        count = re.sub(r'IO.XSRV2.CallbackList.*]\(\"', "", request_num.text.replace("/*<script>location.href='//sina.com';</script>*/\n", "").replace("\");", ""))

        while (flag):
            url = "http://money.finance.sina.com.cn/q/api/jsonp_v2.php/IO.XSRV2.CallbackList['WH4iFBaO9ImEnmgC']/US_ChinaStockService.getData?page="+ str(page) +"&num=60&sort=mktcap&asc=0&market=&concept=0"
            request = requests.get(url, headers=headers)
            request_content = re.sub(r'IO.XSRV2.CallbackList.*]\(', "",
                                     request.text.replace("/*<script>location.href='//sina.com';</script>*/\n",
                                                          "").replace(
                                         ");", ""))
            js = json.loads(request_content)

            n += len(js)

            for stock in js:
                if int(stock['mktcap']) >= market_cap:
                    symbol_name = stock['symbol'] + "_" + stock['name']
                    substock_exist += symbol_name + ","
                    i += 1
                else:
                    flag = False
                    break
            if int(count) == n:
                flag = False

            page += 1

        self.update_us_index_substock_list_exist(102, substock_exist, 'get_us_plate_china_concept_stock_list', i)

    def get_us_plate_other_substock(self):
        market_cap = 20000000000
        stock_list = self.us_stock_service.get_us_stock_with_type_and_market_cap('', market_cap)

        substock_exist = ""
        for stock in stock_list:
            symbol_name = stock['symbol'] + "_" + stock['cname']
            substock_exist += symbol_name + ","

        self.update_us_index_substock_list_exist(103, substock_exist, 'get_us_plate_other_substock_list', len(stock_list))

    def get_us_index_substock_exist(self, id):
        '''
        获取美股指数成份股代码字符串
        :return:
        '''
        stock_exist = self.us_stock_service.get_us_stock_exist(id)
        if stock_exist is None:
            return ""
        if type(stock_exist) is dict:
            return stock_exist.get('symbolstr')

    def update_us_index_substock_list_exist(self, id, us_stock_list_str, type, count):
        '''
        更新所有美股指数成份股代码字符串
        :param us_stock_list_str:
        :param count:
        :return:
        '''
        self.us_stock_service.insert_or_update_us_stock_exist(id, us_stock_list_str, type, count)

if __name__ == '__main__':

    uid = UsIndexesDaily()
    # uid.get_us_indexes_daily("道琼斯指数","2020-08-20","2020-08-28")
    # uid.get_us_indexes_daily("标普500指数", "2020-08-20","2020-08-28")
    # uid.get_us_indexes_daily("纳斯达克综合指数", "2020-08-20","2020-08-28")

    #uid.update_us_three_indexes_daily_lastest()
    uid.get_us_indexes_daily_substock()
    uid.get_us_plate_substock()
    uid.get_us_plate_other_substock()
    uid.get_us_plate_china_concept_stock()

