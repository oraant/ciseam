#coding:utf-8
#!!测试什么时候加载的，应该什么时候关闭cursor
#!!try里面都加上日志什么的
#!!注意，MySQL的增删查改是需要引号的，浏览器传过来的是unicode对象
from django.http import HttpResponse
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
import MySQLdb,json

conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="ciseam",charset='utf8')
cursor = conn.cursor()
cursor.execute("SET NAMES utf8")

# Create your views here.
def index(request):
    #data = delete_user(request)
    data = insert_user(request)
    return HttpResponse(data)
    return HttpResponse(u'欢迎光临CISEAM')

#http://192.168.18.132:8000/filter_user/?id=&user_name=&tel=&qq=&email=&user_comment=
def filter_user(req):
    column=['ID', '姓名', '电话', 'QQ', '邮箱', '备注']
    sql='select id,user_name,tel,qq,email,user_comment from eam_user'

    data=filter_data(sql,req)
    table = format_table(column,data)

    return render(req, 'show_table.html', table)

def update_user(req):
    sql = 'update eam_user'
    msg = update_data(sql,req)
    return msg

def insert_user(req):
    sql = 'insert into eam_user'
    msg = insert_data(sql,req)
    return msg

def delete_user(req):
    sql = 'delete from eam_user'
    msg = delete_data(sql,req)
    return msg

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
def filter_data(sql,req):#don't forget try..catch..else
    request = dict(filter(lambda x: x[1] != '', req.GET.items()))
    sql = sql + ' where 1=1'
    for i in request:
        sql = sql + ' and %s like "%%%s%%"'%(i,request[i])

    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except e:
        print sql
        print e
        data = []

    return data

def update_data(sql,req):#id is not null
    id = req.GET['id']
    request = dict(filter(lambda x: x[1] != '' and x[0] != 'id', req.GET.items()))
    changes = ' and '.join(map(lambda x:'%s="%s"'%(x[0],x[1]),request.items()))
    sql = sql + ' set %s where id=%s'%(changes,id)

    try:
        cursor.execute(sql)
        conn.commit()
        rowcount = cursor.rowcount
    except e:
        print sql
        print e
        rowcount = -1

    if rowcount == 0:
        return '没有找到对应的行'
    elif rowcount == -1:
        return '更新失败'
    else:
        return '更新成功'

def insert_data(sql,req):
    request = dict(filter(lambda x: x[1] != '', req.GET.items()))
    keys = ','.join(request.keys())
    values = ','.join(map(lambda x:'"'+x+'"' if isinstance(x, unicode) else '"'+str(x)+'"',request.values()))

    sql = sql + '(%s) values(%s)'%(keys,values)

    try:
        cursor.execute(sql)
        conn.commit()
        rowcount = cursor.rowcount
    except e:
        print sql
        print e
        rowcount = -1

    if rowcount == 0:
        return '没有找到对应的行'
    elif rowcount == -1:
        return '插入失败'
    else:
        return '插入成功'


def delete_data(sql,req):
    sql = sql + ' where id="%s"'%req.GET['id']

    try:
        cursor.execute(sql)
        conn.commit()
        rowcount = cursor.rowcount
    except e:
        print sql
        print e
        rowcount = -1

    if rowcount == 0:
        return '没有找到对应的行'
    elif rowcount == -1:
        return '删除失败'
    else:
        return '删除成功'


#format return data with json
def format_table(column,data):
    headlist = json.dumps(column)
    bodylist = json.dumps(data, cls=DjangoJSONEncoder)
    table={'headlist':headlist,'bodylist':bodylist}
    return table

def log():
    pass
