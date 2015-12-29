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
    #data = insert_user(request)
    data = filter_attributes(request)
    try:
        return HttpResponse(data)
    except Exception as e:
        return HttpResponse(u'欢迎光临CISEAM')

#------------------------------------------------------------------------------------------------------------------
#http://192.168.18.132:8000/filter_user/?id=&user_name=&tel=&qq=&email=&user_comment=
def filter_user(req):
    column=['用户ID', '姓名', '电话', 'QQ', '邮箱', '备注']

    sql='select id,user_name,tel,qq,email,user_comment from eam_user'
    data=filter_data(sql,req)

    table = format_table(column,data)
    return render(req, 'show_table.html', table)

def update_user(req):
    sql = 'update eam_user'
    msg = update_data(sql,req)
    return HttpResponse(msg)

def insert_user(req):
    sql = 'insert into eam_user'
    msg = insert_data(sql,req)
    return HttpResponse(msg)

def delete_user(req):
    sql = 'delete from eam_user'
    msg = delete_data(sql,req)
    return HttpResponse(msg)

#------------------------------------------------------------------------------------------------------------------
#http://192.168.18.132:8000/filter_asset/?id=&asset_mark=&asset_name=&intake_date=&warranty_period=&price=
def filter_asset(req):
    column=['资产ID', '资产编号', '资产名称', '购买日期', '保修期', '价格']

    sql='select id,asset_mark,asset_name,intake_date,warranty_period,price from eam_asset'
    data=filter_data(sql,req)

    table = format_table(column,data)
    return render(req, 'show_table.html', table)

def update_asset(req):
    sql = 'update eam_asset'
    msg = update_data(sql,req)
    return HttpResponse(msg)

def insert_asset(req):
    sql = 'insert into eam_asset'
    msg = insert_data(sql,req)
    return HttpResponse(msg)

def delete_asset(req):
    sql = 'delete from eam_asset'
    msg = delete_data(sql,req)
    return HttpResponse(msg)

#------------------------------------------------------------------------------------------------------------------
#http://192.168.18.132:8000/filter_attributes/?id=&asset_id=&attribute_key=&attribute_value
def filter_attributes(req):
    column=['资产ID', '资产名称', '资产属性', '资产属性值']

    sql='select b.id,b.asset_name,a.attribute_key,a.attribute_value from eam_attributes a join eam_asset b on a.asset_id=b.id'
    data = filter_data(sql,req)

    table = format_table(column,data)
    return render(req, 'show_table.html', table)

def update_attributes(req):
    sql='update eam_attributes'
    msg = insert_data(sql,req)
    return HttpResponse(msg)

def insert_attributes(req):
    sql = 'insert into eam_attributes'
    msg = insert_data(sql,req)
    return HttpResponse(msg)

def delete_attributes(req):
    sql = 'delete from eam_attributes'
    msg = delete_data(sql,req)
    return HttpResponse(msg)

#------------------------------------------------------------------------------------------------------------------
#http://192.168.18.132:8000/filter_maintenance/?id=&asset_mark=&asset_name=&user_name=&fault_cause=&occur_date=&repair_date=&repair_result=
def filter_maintenance(req):
    column=['ID', '责任人', '设备名称', '设备编号', '故障原因', '故障出现日期', '故障修复日期', '故障修复结果']

    sql='''select a.id,b.user_name,c.asset_name,c.asset_mark,a.fault_cause,a.occur_date,a.repair_date,a.repair_result
           from eam_maintenance a left join eam_user b on (a.user_id = b.id) join eam_asset c on (a.asset_id = c.id)'''
    data = filter_data(sql,req)

    table = format_table(column,data)
    return render(req, 'show_table.html', table)

def update_maintenance(req):
    sql = 'update eam_maintenance'
    msg = update_data(sql,req)
    return HttpResponse(msg)

def insert_maintenance(req):
    sql = 'insert into eam_maintenance'
    msg = insert_data(sql,req)
    return HttpResponse(msg)

def delete_maintenance(req):
    sql = 'delete from eam_maintenance'
    msg = delete_data(sql,req)
    return HttpResponse(msg)

#------------------------------------------------------------------------------------------------------------------
#http://192.168.18.132:8000/filter_usagerecord?id=&asset_name=&asset_mark&user_name=&begin_date=&end_date
def filter_usagerecord(req):
    column=['记录ID', '设备名称', '设备编号', '使用用户', '开始使用日期', '归还日期']
    sql='select a.id,c.asset_name,c.asset_mark,b.user_name,a.begin_date,a.end_date from eam_usagerecord a left join eam_user b on (a.user_id = b.id) join eam_asset c on (a.asset_id = c.id)'
    data = filter_data(sql,req)

    table = format_table(column,data)
    return render(req, 'show_table.html', table)

def update_usagerecord(req):
    sql = 'update eam_usagerecord'
    msg = update_data(sql,req)
    return HttpResponse(msg)

def insert_usagerecord(req):
    sql = 'insert into eam_usagerecord'
    msg = insert_data(sql,req)
    return HttpResponse(msg)

def delete_usagerecord(req):
    sql = 'delete from eam_usagerecord'
    msg = delete_data(sql,req)
    return HttpResponse(msg)

#------------------------------------------------------------------------------------------------------------------
#format sql with where condition,and fetch data
def filter_data(sql,req,exact=False):#don't forget try..catch..else
    request = dict(filter(lambda x: x[1] != '', req.GET.items()))
    sql = sql + ' where 1=1'
    for i in request:
        sql = sql + ' and %s="%s"'%(i,request[i]) if exact else sql + ' and %s like "%%%s%%"'%(i,request[i])

    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as e:
        print sql
        print e
        data = []

    return data

def update_data(sql,req):#id is not null
    try:
        id = req.GET['id']
    except:
        return '没有指定要更新的ID'

    request = dict(filter(lambda x: x[1] != '' and x[0] != 'id', req.GET.items()))#去掉空参数，和名为ID的参数
    changes = ','.join(map(lambda x:'%s="%s"'%(x[0],x[1]),request.items()))#排列要更新的列和值

    sql = sql + ' set %s where id=%s'%(changes,id)
    return execute(sql)

#make sure the not null column is not null
def insert_data(sql,req):
    request = req.GET
    keys = ','.join(request.keys())#排列插入时有哪些列的值
    values = map(lambda x:'"'+x+'"' if isinstance(x, unicode) else '"'+str(x)+'"',request.values())#把unicode值和int值转成带双引号的字符串
    values = map(lambda x:'NULL' if x=='""' else x,values)#把空值转换为不带引号的NULL值
    values = ','.join(values)

    sql = sql + '(%s) values(%s)'%(keys,values)
    return sql
    return execute(sql)

#only need id parameter
def delete_data(sql,req):
    try:
        sql = sql + ' where id="%s"'%req.GET['id']
    except:
        return '没有指定要删除的ID'
    return execute(sql)

def execute(sql):
    try:
        cursor.execute(sql)
        conn.commit()
        return '没有找到对应的行' if cursor.rowcount==0 else '执行成功'
    except Exception as e:
        return u'执行失败<br>SQL:%s<br>Exception:%s'%(sql,str(e))

#format return data with json
def format_table(column,data):
    headlist = json.dumps(column)
    bodylist = json.dumps(data, cls=DjangoJSONEncoder)
    table={'headlist':headlist,'bodylist':bodylist}
    return table

def log():
    pass
