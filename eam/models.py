#coding:utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=10)
    tel = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    qq = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    user_comment = models.CharField(max_length=3000, blank=True, null=True)

    def __unicode__(self):
        return '%d,%s,%s'%(self.id, self.user_name, self.user_comment)
    def keys(self):
        return ["用户ID", "用户名", "电话", "QQ号", "邮箱", "备注"]
    def values(self):
        return [self.id, self.user_name, self.tel, self.qq, self.email, self.user_comment]


class Asset(models.Model):
    asset_mark = models.CharField(max_length=300)
    asset_name = models.CharField(max_length=300)
    intake_date = models.DateField(blank=True, null=True)
    warranty_period = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __unicode__(self):
        return '%d,%s,%s'%(self.id, self.asset_name, self.asset_mark)
    def keys(self):
        return ["资产ID", "资产编号", "资产名称", "购买日期", "保修期", "价格"]
    def values(self):
        return [self.id, self.asset_mark, self.asset_name, self.intake_date, self.warranty_period, self.price]


class Attributes(models.Model):
    asset_id = models.ForeignKey(Asset)
    attribute_key = models.CharField(max_length=300)
    attribute_value = models.CharField(max_length=300)

    def __unicode__(self):
        return '%d,%s,%s'%(self.id, self.attribute_key, self.attribute_value)
    def keys(self):
        return ["属性ID", "资产编号", "资产属性", "资产属性值"]
    def values(self):
        return [self.id, self.asset_id, self.attribute_key, self.attribute_value]


class UsageRecord(models.Model):
    asset_id = models.ForeignKey(Asset)
    user_id = models.ForeignKey(User)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return '%d,%s,%s'%(self.id, self.asset_id, self.user_id)
    def keys(self):
        return ["记录ID", "资产ID", "用户ID", "开始使用时间", "归还时间"]
    def values(self):
        return [self.id, self.asset_id, self.user_id, self.begin_date, self.end_date]


class Maintenance(models.Model):
    asset_id = models.ForeignKey(Asset)
    user_id = models.ForeignKey(User, blank=True, null=True)
    fault_cause = models.CharField(max_length=3000)
    occur_date = models.DateField()
    repair_date = models.DateField(blank=True, null=True)
    repair_result = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%d,%s,%s,%s'%(self.id, self.asset_id, self.user_id, self.fault_cause)
    def keys(self):
        return ["记录ID", "资产ID", "用户ID", "故障原因", "出现日期", "修复日期", "修复结果"]
    def values(self):
        return [self.id, self.asset_id, self.user_id, self.fault_cause, self.occur_date, self.repair_date, self.repair_result]
