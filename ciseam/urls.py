"""ciseam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from eam import views as eam_v

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', eam_v.index),

    url(r'^filter_user/', eam_v.filter_user),
    url(r'^update_user/', eam_v.update_user),
    url(r'^delete_user/', eam_v.delete_user),
    url(r'^insert_user/', eam_v.insert_user),

    url(r'^filter_asset/', eam_v.filter_asset),
    url(r'^update_asset/', eam_v.update_asset),
    url(r'^delete_asset/', eam_v.delete_asset),
    url(r'^insert_asset/', eam_v.insert_asset),

    url(r'^filter_attributes/', eam_v.filter_attributes),
    url(r'^update_attributes/', eam_v.update_attributes),
    url(r'^delete_attributes/', eam_v.delete_attributes),
    url(r'^insert_attributes/', eam_v.insert_attributes),

    url(r'^filter_maintenance/', eam_v.filter_maintenance),
    url(r'^update_maintenance/', eam_v.update_maintenance),
    url(r'^delete_maintenance/', eam_v.delete_maintenance),
    url(r'^insert_maintenance/', eam_v.insert_maintenance),

    url(r'^filter_usagerecord/', eam_v.filter_usagerecord),
    url(r'^update_usagerecord/', eam_v.update_usagerecord),
    url(r'^delete_usagerecord/', eam_v.delete_usagerecord),
    url(r'^insert_usagerecord/', eam_v.insert_usagerecord),
]
