#coding=utf-8
__author__ = 'yangkai'

# 独立使用django的model

import sys
import os



pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + '../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")

import django
django.setup()

from goods.models import GoodsCategory

from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    lev1_category = GoodsCategory()
    lev1_category.name = lev1_cat['name']
    lev1_category.code = lev1_cat['code']
    lev1_category.category_type = 1
    lev1_category.save()
    for lev2_cat in lev1_cat['sub_categorys']:
        lev2_category = GoodsCategory()
        lev2_category.name = lev2_cat['name']
        lev2_category.code = lev2_cat['code']
        lev2_category.category_type = 2
        lev2_category.parent_category = lev1_category
        lev2_category.save()
        for lev3_cat in lev2_cat['sub_categorys']:
            lev3_category = GoodsCategory()
            lev3_category.name = lev3_cat['name']
            lev3_category.code = lev3_cat['code']
            lev3_category.category_type = 3
            lev3_category.parent_category = lev2_category
            lev3_category.save()
