# coding:utf-8
# Author:Dzer0
# 测试
import time # 时间
import MySQLdb
from jiankong import send_mail, jiance
from apscheduler.schedulers.blocking import BlockingScheduler # 定时运行命令
from mysql_sy import create_or_update_mysql # 写入日志
import threading # 使用线程
from tongji import mysql_zhengli

def cron_task():
    sched = BlockingScheduler()
    sched.add_job(mysql_zhengli, 'cron', day_of_week=1, hour=11, minute=03,end_date='2114-05-30')
    #sched.add_job(reset_mysql, 'cron', day_of_week=4, hour=16, minute=59,end_date='2114-05-30')
    sched.start()
if __name__ == '__main__':
    t = threading.Thread(target=cron_task)
    t.start()