#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import MySQLdb

conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="ciseam",charset='utf8')
cursor = conn.cursor()
cursor.execute("SET NAMES utf8")

# Create your views here.
def index(request):
    return HttpResponse(u'欢迎光临CISEAM')

#http://192.168.18.132:8000/filter_user/?id=&user_name=&tel=&qq=&email=&user_comment=
def filter_user(req):
    sql='select * from eam_user'
    return filter_data(sql,req)

#http://192.168.18.132:8000/filter_asset/?id=&asset_mark=&asset_name=&intake_date=&warranty_period=&price=
def filter_asset(req):
    sql='select * from eam_asset'
    return filter_data(sql,req)

#http://192.168.18.132:8000/filter_attributes/?id=&asset_id=&attribute_key=&attribute_value
def filter_attributes(req):
    sql='select * from eam_attributes'
    return filter_data(sql,req)

#http://192.168.18.132:8000/filter_maintenance/?id=&asset_id=&user_id=&fault_cause=&occur_date=&repair_date=&repair_result=
def filter_maintenance(req):
    sql='select * from eam_maintenance'
    return filter_data(sql,req)

#http://192.168.18.132:8000/filter_usagerecord?id=&asset_id=&user_id=&begin_date=&end_date
def filter_usagerecord(req):
    sql='select * from eam_usagerecord'
    return filter_data(sql,req)

#format sql with where condition,and fetch data
def filter_data(sql,req):
    request = dict(filter(lambda x: x[1] != '', req.GET.items()))
    sql = sql + ' where 1=1'
    for i in request:
            sql = sql + ' and %s like "%%%s%%"'%(i,request[i])
    cursor.execute(sql)
    data = cursor.fetchall()
    return HttpResponse(data)
