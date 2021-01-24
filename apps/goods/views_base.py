#coding=utf-8
__author__ = 'yangkai'

from django.views.generic.base import View
# from django.views.generic import ListView
from .models import Goods
import json
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core.serializers import serialize



class GoodsListView(View):
    def get(self, request):
        '''
        通过django的view实现商品列表页
        :param request:
        :return:
        '''
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)
        json_data = serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)
