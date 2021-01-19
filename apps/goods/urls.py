# from django.contrib import admin
from django.conf.urls import url, include
from django.views.static import serve
from MxShop.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    url(r'list/$', name='goods_list')
]
