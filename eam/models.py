#coding:utf-8
from django.db import models

# Create your models here.
class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    asset_serial = models.CharField(max_length=100)
    intake_date = models.DateField(blank=True, null=True)
    warranty_period = models.CharField(max_length=30,blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return '%d,%s,%s'%(self.id, self.asset_name, self.asset_serial)


class Attributes(models.Model):
    asset = models.ForeignKey(Asset)
    attr_key = models.CharField(max_length=100)
    attr_value = models.CharField(max_length=100)

    def __unicode__(self):
        return '%d,%s,%s'%(self.id, self.attr_key, self.attr_value)


class User(models.Model):
    user_name = models.CharField(max_length=30)
    tel = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    qq = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    comments = models.CharField(max_length=3000, blank=True, null=True)

    def __unicode__(self):
        return '%d,%s,%s'%(self.id, self.user_name, self.comments)


class Maintenance(models.Model):
    asset = models.ForeignKey(Asset)
    user = models.ForeignKey(User, blank = True, null=True)
    fault_cause = models.CharField(max_length=3000)
    repair_time = models.DateField()
    repair_result = models.CharField(max_length=500)

    def __unicode__(self):
        return '%d,%s,%s,%s'%(self.id, self.asset, self.user, self.cause)


class UsageRecord(models.Model):
    asset = models.ForeignKey(Asset)
    user = models.ForeignKey(User)
    begin_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return '%d,%s,%s'%(self.id, self.asset, self.user)

