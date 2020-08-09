from com.swordfall.utils.SchedulerUtils import SchedulerUtils
from com.swordfall.trade.hk.HangSengIndexesDaily import HangSengIndexesDaily
from com.swordfall.trade.hk.HkStockDaily import HkStockDaily
from com.swordfall.trade.hk.HkStockList import HkStockList

from com.swordfall.trade.us.UsIndexesDaily import UsIndexesDaily
from com.swordfall.trade.us.UstockList import UstockList
from com.swordfall.trade.us.UstockDaily import UstockDaily

class SchedulerJobs:

    def __init__(self):
        self.schedulerUtils = SchedulerUtils()
        self.hangSengIndexesDaily = HangSengIndexesDaily()
        self.hkStockDaily = HkStockDaily()
        self.hkStockList = HkStockList()

        self.usIndexesDaily = UsIndexesDaily()
        self.ustockList = UstockList()
        self.ustockDaily = UstockDaily()

    def add_hk_job(self):
        print("SchedulerJobs update_hk_hang_seng_index_daily_lastest 每天更新恒生指数行情")
        self.schedulerUtils.timer_scheduler(job=self.hangSengIndexesDaily.update_hk_hang_seng_index_daily_lastest, day_of_week='0-5', hour=16, minute=30)
        print("SchedulerJobs get_hk_all_stock_list_daily 每天更新港股列表")
        self.schedulerUtils.timer_scheduler(job=self.hkStockList.get_hk_all_stock_list_daily(), day_of_week='0-5', hour=9, minute=32)
        print("SchedulerJobs update_hk_all_stock_daily_lastest 更新所有港股今天行情")
        self.schedulerUtils.timer_scheduler(job=self.hkStockDaily.update_hk_all_stock_daily_lastest(), day_of_week='0-5', hour=16, minute=30)

    def add_us_job(self):
        print("SchedulerJobs update_us_three_indexes_daily_lastest 每天更新美股三大指数行情")
        self.schedulerUtils.timer_scheduler(job=self.usIndexesDaily.update_us_three_indexes_daily_lastest(), day_of_week='1-6', hour=4, minute=30)
        print("SchedulerJobs get_ustock_list 每天更新美股列表")
        self.schedulerUtils.timer_scheduler(job=self.ustockList.get_ustock_list(), day_of_week='0-5', hour=22, minute=00)
        print("SchedulerJobs get_ustock_list 每天更新美股列表")
        self.schedulerUtils.timer_scheduler(job=self.ustockDaily.update_us_all_stock_daily_lastest(), day_of_week='1-6', hour=4, minute=35)

    def add_hk_stock_up_job(self):
        print("SchedulerJobs ")

if __name__ == "main":
    sj = SchedulerJobs()
    sj.add_hk_job()
    sj.add_us_job()
    sj.schedulerUtils.start()