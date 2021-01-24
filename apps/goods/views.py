from django.shortcuts import render
from rest_framework import filters
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .filters import GoodsFilter
from django_filters.rest_framework import DjangoFilterBackend


from .serializers import GoodsSerializer, GoodCategorySerializer
from .models import Goods, GoodsCategory


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    page_size_query_param = 'skip'
    max_page_size = 1000


# Create your views here.
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页, 分页，排序，搜索，筛选
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = StandardResultsSetPagination
    # filter_backends = (DjangoFilterBackend, )
    # filterset_class = GoodsFilter
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filter_class = GoodsFilter
    search_fields = ['name', 'goods_desc', 'goods_brief']
    ordering_fields = ('sold_num', 'shop_price')


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    '''
    list:
        获取全部的商品分类数据
    '''
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = GoodCategorySerializer


class CategoryDetailViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    list:
        获取单个大分类的商品分类数据
    '''
    queryset = GoodsCategory.objects.filter(parent_category=1)
    serializer_class = GoodCategorySerializer
