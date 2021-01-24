#coding=utf-8
__author__ = 'yangkai'

from rest_framework import serializers
from .models import GoodsCategory, Goods


class GoodCategorySerializer2(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodCategorySerializer1(serializers.ModelSerializer):
    sub_cat = GoodCategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodCategorySerializer(serializers.ModelSerializer):
    sub_cat = GoodCategorySerializer1(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodCategorySerializer()

    class Meta:
        model = Goods
        fields = '__all__'