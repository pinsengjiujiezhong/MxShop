#coding=utf-8
__author__ = 'yangkai'

import django_filters
from django.db.models import Q
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category=value) | Q(category__parent_category__parent_category=value))


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'name']


