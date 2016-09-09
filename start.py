# coding:utf-8
# Author:Dzer0
# 启动
import time # 时间
import MySQLdb
from jiankong import send_mail, jiance
from apscheduler.schedulers.blocking import BlockingScheduler # 定时运行命令
from tongji import mysql_zhengli
import threading # 使用线程
import urllib2
from mysql_sy import create_or_update_mysql # 写入日志

def conMysql():
    '''
        连接数据库，并读取内容
    '''
    c = MySQLdb.connect('SQL数据库链接地址','账户','密码','库名',3306,charset='utf8')
    cursor = c.cursor()
    count = cursor.execute('select * from project')
    print('共有%s条信息' % count)
    # 获取所有记录
    print('获取所有记录')
    result = cursor.fetchmany(count)
    c.commit()
    cursor.close()
    c.close()
    return result

def reset_mysql():
    print('mysql数据库日志重置')
    db = MySQLdb.connect('SQL数据库链接地址','账户','密码','库名',3306,charset='utf8')
    cursor = db.cursor()
    sql = "truncate table logs"
    print sql
    try:
        cursor.execute(sql)
        db.autocommit()
    except:
        db.rollback()
    db.close()

# 短信平台监控上班
def sms_sb():
    jy = '"0"'
    headers = {'Content-Type' : 'application/json'}
    url = "http://短信接口地址"
    sb = '{invokerId:"100010",templateId:"4",destinationNumber:"手机号",password:"key",isInstant:"true",args:[    "起床上班!"]}'
    print('短信监测启动')
    print jy
    req = urllib2.Request(url, sb, headers)
    response =urllib2.urlopen(req)
    context = response.read()
    print context
    if jy in context:
        print('success')
        create_or_update_mysql('SMS短信平台',str('success_count'))

# 短信平台监控下班发送短信
def sms_xb():
    jy = '"0"'
    headers = {'Content-Type' : 'application/json'}
    url = "http://短信接口地址"
    sb = '{invokerId:"100010",templateId:"4",destinationNumber:"手机号",password:"key",isInstant:"true",args:[    "下班打卡!"]}'
    print('短信监测启动')
    print jy
    req = urllib2.Request(url, sb, headers)
    response =urllib2.urlopen(req)
    context = response.read()
    print context
    if jy in context:
        print('success')
        create_or_update_mysql('SMS短信平台',str('success_count'))

def cron_task():
    print('后台定时运行任务已经启动')
    sched = BlockingScheduler()
    sched.add_job(mysql_zhengli, 'cron', day_of_week=4, hour=16, minute=50,end_date='2114-05-30')
    sched.add_job(reset_mysql, 'cron', day_of_week=4, hour=17, minute=10,end_date='2114-05-30')
    sched.add_job(sms_sb, 'cron', day_of_week='0-6', hour=8, minute=50,end_date='2114-05-30')
    sched.add_job(sms_xb, 'cron', day_of_week='0-6', hour=17, minute=00,end_date='2114-05-30')
    sched.start()


if __name__ == '__main__':
    t = threading.Thread(target=cron_task)
    t.start()
    while 1:
        a = conMysql()
	for i in a:
            if i[10].encode('utf8')=='1':
		print('检测' + i[1].encode('utf8'))
                jiance(i)
            else:
		print('跳过检测' + i[1].encode('utf8'))
        #for i in a:
        #    jiance(i)
        print('等待5分钟后继续监听')
        time.sleep(5*60)
