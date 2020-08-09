
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

class SchedulerUtils:

    def __init__(self):
        self.scheduler = BlockingScheduler()


    def random_time(self):
        #print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return datetime.now().strftime("%Y%m%d%H%M%S")

    def interval_scheduler(self, job, type, interval):
        id_str = type + "_" + str(interval) + "_" + self.random_time()
        if type is 'minutes':
            self.scheduler.add_job(func=job, trigger='interval', minutes=interval, id=id_str)
        if type is 'seconds':
            self.scheduler.add_job(func=job, trigger='interval', seconds=interval, id=id_str)

    def timer_scheduler(self, job, day_of_week, hour, minute):
        id_str = day_of_week + "_" + hour + "_" + minute + "_" + self.random_time()
        self.scheduler.add_job(func=job, trigger='cron', day_of_week=day_of_week, hour=hour, minute=minute, id=id_str)

    def start(self):
        self.scheduler.start()


if __name__ == '__main__':
    sj = SchedulerUtils()
    #sj.interval_scheduler(sj.test_job)
    sj.test_job()
