from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from goods.models import Goods
from datetime import datetime

User = get_user_model()


class ShoppingCart(models.Model):
    '''
    购物车
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品')
    goods_num = models.IntegerField(default=0, verbose_name='数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s(%d)'.format(self.goods.name, self.goods_num)


class OrderInfo(models.Model):
    '''
    订单
    '''
    ORDER_STATUS = (('success', '成功'), ('cancel', '取消'), ('wait', '待支付'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    order_sn = models.CharField(max_length=200, unique=True, verbose_name='订单编号')
    trade_no = models.CharField(max_length=200, unique=True, verbose_name='支付订单编号')
    pay_status = models.CharField(max_length=20, verbose_name='支付状态', choices=ORDER_STATUS)
    order_mount = models.FloatField(default=0, verbose_name='订单金额')
    post_script = models.CharField(max_length=200, )
    pay_time = models.DateTimeField(default='', verbose_name='支付时间')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    '''
    订单的商品详情
    '''
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, verbose_name='订单信息')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品信息')
    goods_num = models.IntegerField(default=0, verbose_name='商品数量')

    class Meta:
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
