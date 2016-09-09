# coding:utf-8
# Author:Dzer0
# 操作数据库
import time # 时间
import MySQLdb


def insert_mysql(a,b,c):
    db = MySQLdb.connect('数据库连接地址','用户名','密码','库名',3306,charset='utf8')
    cursor = db.cursor()
    sql = "insert into logs (projectname, error_count, success_count) values('"+ a +"',"+str(b)+","+str(c)+")"
    print sql
    try:
        cursor.execute(sql)
        db.autocommit()
    except:
        db.rollback()
    db.close()

def create_or_update_mysql(projectname,success_or_faid):
    db = MySQLdb.connect('数据库连接地址','用户名','密码','库名',3306,charset='utf8')
    cursor = db.cursor()
    sql_select = "select * from logs where projectname = '" + projectname+"'"
    sql_insert = "insert into logs (projectname, error_count, success_count) values('"+ projectname +"',"+str(0)+","+str(1)+")"
    sql_update_error = "update logs set error_count = error_count + 1 where projectname = '" + projectname + "'"
    sql_update_success = "update logs set success_count = success_count + 1 where projectname = '" + projectname + "'"
    #print sql_select
    cursor.execute(sql_select)
    results = cursor.fetchall()
    if results <> ():
        if success_or_faid=='error_count':
            cursor.execute(sql_update_error)
        else:
            cursor.execute(sql_update_success)
    else:
        print('数据不存在插入数据')
        cursor.execute(sql_insert)
    db.commit()
    db.close()

if __name__ == '__main__':
    #insert_mysql('asdfasdf',0,0)
    create_or_update_mysql('12312312','error_count')