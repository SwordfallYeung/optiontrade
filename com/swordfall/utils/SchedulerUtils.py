
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

class SchedulerUtils:


    def test_job(self):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def interval_scheduler(self, job):
        scheduler = BlockingScheduler()
        scheduler.add_job(func=job, trigger='interval', seconds=10, id='test_job1')
        scheduler.start()

    def timer_scheduler(self, job):
        scheduler = BlockingScheduler()
        scheduler.add_job(func=job, trigger='cron', day_of_week='0-5', hour=16, minute=30, id='test_job2')
        scheduler.start()

if __name__ == '__main__':
    sj = SchedulerUtils()
    sj.interval_scheduler(sj.test_job)
