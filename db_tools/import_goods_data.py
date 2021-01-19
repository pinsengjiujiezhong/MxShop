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

from goods.models import Goods, GoodsCategory, GoodsImage

from db_tools.data.product_data import row_data

for good_cat in row_data:
    goods = Goods()
    goods.name = good_cat['name']
    goods.market_price = float(good_cat['market_price'].replace('￥', '').replace('元', ''))
    goods.shop_price = float(good_cat['sale_price'].replace('￥', '').replace('元', ''))
    goods.good_brief = good_cat['desc'] if good_cat['desc'] is None else ''
    goods.good_desc = good_cat['goods_desc'] if good_cat['goods_desc'] is None else ''
    goods.goods_front_image = good_cat['images'][0] if good_cat['images'] else ''
    category_name = good_cat["categorys"][-1]
    categorys = GoodsCategory.objects.filter(name=category_name)
    if categorys:
        goods.category = categorys[0]
    goods.save()
    for goods_img in good_cat['images']:
        images = GoodsImage()
        images.goods = goods
        images.image = goods_img
        images.save()

