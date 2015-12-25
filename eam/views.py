#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render
import eam.models as m

# Create your views here.
def index(request):
    #test = filter_attributes(request)
    #test = filter_user(request)
    #test = filter_maintenance(request)
    #test = filter_asset(request)
    #test = filter_usagerecord(request)
    return HttpResponse(test)

    #return HttpResponse(u"北京中研软科技有限公司 资产管理系统")

#http://192.168.18.132:8000/?id=&user_name=&tel=&qq=&email=&user_comment=
def filter_user(req):
    id = req.GET['id']
    user_name = req.GET['user_name']
    tel = req.GET['tel']
    qq = req.GET['qq']
    email = req.GET['email']
    user_comment = req.GET['user_comment']

    users = m.User.objects.filter(id__contains=id)
    users = users.filter(user_name__contains=user_name)
    users = users if tel=='' else users.filter(tel__contains=tel)
    users = users if qq=='' else users.filter(qq__contains=qq)
    users = users if email=='' else users.filter(email__contains=email)
    users = users if user_comment=='' else users.filter(user_comment__contains=user_comment)

    return users

#http://192.168.18.132:8000/?id=&asset_mark=&asset_name=&intake_date=&warranty_period=&price=
def filter_asset(req):
    id = req.GET['id']
    asset_mark = req.GET['asset_mark']
    asset_name = req.GET['asset_name']
    intake_date = req.GET['intake_date']
    warranty_period = req.GET['warranty_period']
    price = req.GET['price']

    assets = m.Asset.objects.filter(id__contains=id)
    assets = assets.filter(asset_mark__contains=asset_mark)
    assets = assets.filter(asset_name__contains=asset_name)
    assets = assets if intake_date=='' else assets.filter(intake_date__contains=intake_date)
    assets = assets if warranty_period=='' else assets.filter(warranty_period__contains=warranty_period)
    assets = assets if price=='' else assets.filter(price__contains=price)

    return assets

#http://192.168.18.132:8000/?id=&asset_id=&attribute_key=&attribute_value
def filter_attributes(req):
    id = req.GET['id']
    asset_id = req.GET['asset_id']
    attribute_key = req.GET['attribute_key']
    attribute_value = req.GET['attribute_value']
    
    attrs = m.Attributes.objects.filter(id__contains=id)
    attrs = attrs.filter(asset__id__contains=asset_id)
    attrs = attrs.filter(attribute_key__contains=attribute_key)
    attrs = attrs.filter(attribute_value__contains=attribute_value)

    return attrs

#http://192.168.18.132:8000/?id=&asset_id=&user_id=&fault_cause=&occur_date=&repair_date=&repair_result=
def filter_maintenance(req):

    id = req.GET['id']
    asset_id = req.GET['asset_id']
    user_id = req.GET['user_id']
    fault_cause = req.GET['fault_cause']
    occur_date = req.GET['occur_date']
    repair_date = req.GET['repair_date']
    repair_result  = req.GET['repair_result']

    mains = m.Maintenance.objects.filter(id__contains=id)
    mains = mains.filter(asset__id__contains=asset_id)
    mains = mains.filter(fault_cause__contains=fault_cause)
    mains = mains.filter(occur_date__contains=occur_date)
    mains = mains if user_id=='' else mains.filter(user__id__contains=user_id)
    mains = mains if repair_date=='' else mains.filter(repair_date__contains=repair_date)
    mains = mains if repair_result=='' else mains.filter(repair_result__contains=repair_result)

    return mains

#http://192.168.18.132:8000/?id=&asset_id=&user_id=&begin_date=&end_date
def filter_usagerecord(req):
    id = req.GET['id']
    asset_id = req.GET['asset_id']
    user_id = req.GET['user_id']
    begin_date = req.GET['begin_date']
    end_date = req.GET['end_date']

    records = m.UsageRecord.objects.filter(id__contains=id)
    records = records.filter(asset__id__contains=asset_id)
    records = records.filter(user__id__contains=user_id)
    records = records.filter(begin_date__contains=begin_date)
    records = records if end_date=='' else records.filter(end_date__contains=end_date)

    return records
