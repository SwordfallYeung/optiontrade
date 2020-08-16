from com.swordfall.utils.ApsSchedulerUtils import ApsSchedulerUtils
from com.swordfall.trade.hk.HangSengIndexesDaily import HangSengIndexesDaily
from com.swordfall.trade.hk.HkStockDaily import HkStockDaily
from com.swordfall.trade.hk.HkStockList import HkStockList

from com.swordfall.trade.us.UsIndexesDaily import UsIndexesDaily
from com.swordfall.trade.us.UstockList import UstockList
from com.swordfall.trade.us.UstockDaily import UstockDaily

from com.swordfall.core.StockTrend import StockTrend
from com.swordfall.utils.CommonUtils import CommonUtils
import time
import schedule
import threading

class SchedulerJobs:

    def __init__(self):
        self.apsSchedulerUtils = ApsSchedulerUtils()
        self.hangSengIndexesDaily = HangSengIndexesDaily()
        self.hkStockDaily = HkStockDaily()
        self.hkStockList = HkStockList()

        self.usIndexesDaily = UsIndexesDaily()
        self.ustockList = UstockList()
        self.ustockDaily = UstockDaily()

        self.stockTrend = StockTrend()
        self.commonUtils = CommonUtils()

    def run_daemon_thread(self, job, method_type, run_type):
        job_thread = threading.Thread(target=job(method_type, run_type))
        job_thread.setDaemon(True)
        job_thread.start()

    def hk_stock_service(self, method_type, run_type):
        if run_type == 'interval':
            flag = True
            while (flag):
                if method_type == 'index':
                    self.hangSengIndexesDaily.update_hk_hang_seng_index_daily_lastest()
                elif method_type == 'daily':
                    self.hkStockDaily.update_hk_all_stock_daily_lastest()
                time.sleep(15 * 60)
                flag = self.commonUtils.get_china_hk_weekdays_time()
        elif run_type == 'only':
            if method_type == 'list':
                self.hkStockList.get_hk_all_stock_list_daily()

    def add_hk_job_schedule(self):
        schedule.every().day.at("9:30").do(self.run_daemon_thread, self.hk_stock_service, 'index', 'interval')
        schedule.every().day.at("9:30").do(self.run_daemon_thread, self.hk_stock_service, 'list', 'only')
        schedule.every().day.at("9:30").do(self.run_daemon_thread, self.hk_stock_service, 'daily', 'interval')


    def add_hk_job_aps(self):
        self.apsSchedulerUtils.timer_scheduler(job=self.hangSengIndexesDaily.update_hk_hang_seng_index_daily_lastest, day_of_week='0-5', hour=23, minute=00)
        self.apsSchedulerUtils.timer_scheduler(job=self.hkStockList.get_hk_all_stock_list_daily, day_of_week='0-6', hour=16, minute=37)
        self.apsSchedulerUtils.timer_scheduler(job=self.hkStockDaily.update_hk_all_stock_daily_lastest, day_of_week='0-5', hour=23, minute=5)

    def us_stock_service(self, method_type, run_type):
        if run_type == 'interval':
            flag = True
            while (flag):
                if method_type == 'index':
                    self.usIndexesDaily.update_us_three_indexes_daily_lastest()
                elif method_type == 'daily':
                    self.ustockDaily.update_us_all_stock_daily_lastest()
                time.sleep(15 * 60)
                flag = self.commonUtils.get_us_weekdays_time()
        elif run_type == 'only':
            if method_type == 'list':
                self.ustockList.get_ustock_list()

    def add_us_job_schedule(self):
        schedule.every().day.at("21:30").do(self.run_daemon_thread, self.us_stock_service, 'index', 'interval')
        schedule.every().day.at("21:30").do(self.run_daemon_thread, self.us_stock_service, 'list', 'only')
        schedule.every().day.at("21:30").do(self.run_daemon_thread, self.us_stock_service, 'daily', 'interval')

    def add_us_job_aps(self):
        self.apsSchedulerUtils.timer_scheduler(job=self.usIndexesDaily.update_us_three_indexes_daily_lastest, day_of_week='1-6', hour=4, minute=30)
        self.apsSchedulerUtils.timer_scheduler(job=self.ustockList.get_ustock_list, day_of_week='0-5', hour=1, minute=36)
        self.apsSchedulerUtils.timer_scheduler(job=self.ustockDaily.update_us_all_stock_daily_lastest, day_of_week='1-6', hour=4, minute=35)

    def add_hk_stock_up_job(self):
        print("SchedulerJobs all_stock_trend 计算所有港股上升趋势的个数")
        self.stockTrend.all_stock_trend()

if __name__ == '__main__':
    sj = SchedulerJobs()
    #sj.add_hk_job_schedule()
    #sj.add_us_job_schedule()
    sj.add_hk_stock_up_job()

    while True:
        schedule.run_pending()
        time.sleep(1)
