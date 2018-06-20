#!/usr/bin/python
#coding-utf8

import pymssql

server = "172.18.20.60"         #连接服务器地址
user = "monitor"                #连接账号
password = "monitor"            #连接密码

conn = pymssql.connect(server, user, password, "donghuan")      #获取连接
cur = conn.cursor()			#获取光标

#查询表
cur.execute('select * from persons where salesrep=%s')

print (cur.fetchall())

cur.close()

conn.close()
