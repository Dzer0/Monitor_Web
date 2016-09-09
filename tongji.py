# coding:utf-8
# Author:Dzer0
# 测试
import time # 时间
import MySQLdb
from jiankong import send_mail, jiance
from apscheduler.schedulers.blocking import BlockingScheduler # 定时运行命令


def mysql_zhengli():
    mailto_list=["接收周报邮箱"]  # 接收邮件列表
    c = MySQLdb.connect('数据库连接地址','用户名','密码','库名',3306,charset='utf8')
    cursor = c.cursor()
    count = cursor.execute('select * from logs')
    print('共有%s条信息' % count)
    result = cursor.fetchmany(count)
    c.commit()
    cursor.close()
    c.close()
    context = '<h3>运维检测周报</h3>\n'
    for i in result:
        error = float(i[2])
        success = float(i[3])
        zongshu = error + success
        #print zongshu,error,success
        bfb = success/zongshu
        #print bfb
        nr = "<p>"+str(i[1].encode('utf8')) + "本周共检测"+ str(int(zongshu)) +"次;项目正确率是：%.2f%%"  %(bfb*100)+'\n</p>'
        context = context+nr
    print('发送定时邮件')
    send_mail(mailto_list,'运维项目检测周报', context)
    return context

if __name__ == '__main__':
    a = mysql_zhengli()
    print a
