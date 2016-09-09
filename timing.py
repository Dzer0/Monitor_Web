# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
def my_job():
    print 'hello world!!!!!!!!!!'

sched = BlockingScheduler()
# sched.add_job(my_job, 'interval', seconds=5)
sched.add_job(my_job, 'cron', day_of_week=0, hour=13, minute=59,end_date='2114-05-30')
# interval 间隔调度 每个几秒执行一次
# cron定时调度 什么时间执行，在结束时间前循环执行
# date定时调度 什么时间执行，只执行一次
sched.start()