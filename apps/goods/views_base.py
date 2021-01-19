#coding=utf-8
__author__ = 'yangkai'

from django.views.generic.base import View
# from django.views.generic import ListView
from .models import Goods

class goodsListView(View):
    def get(self, request):
        '''
        通过django的view实现商品列表页
        :param request:
        :return:
        '''
        goods = Goods.objects.all()[:10]


