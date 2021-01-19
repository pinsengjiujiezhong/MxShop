from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from goods.models import Goods
from datetime import datetime

User = get_user_model()


class UserFav(models.Model):
    '''
    用户收藏
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    '''
    用户留言
    '''
    MESSAGE_CHIOCES = ((1, '留言'), (2, '投诉'), (3, '询问'), (4, '售后'), (5, '求购'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHIOCES, verbose_name='留言类型', help_text=u'留言类型: 1(留言),2(投诉),3(询问),4(售后), 5(求购)')
    message = models.TextField(verbose_name='留言内容', default='', help_text='留言内容')
    subject = models.CharField(max_length=100, default='', verbose_name='留言主题')
    file = models.FileField(verbose_name='上传文件', help_text='上传文件')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    '''
    用户收货地址
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    district = models.CharField(max_length=100, default='', verbose_name='区域')
    address = models.CharField(max_length=100, default='', verbose_name='详细地址')
    signer_name = models.CharField(max_length=100, default='', verbose_name='签收人')
    signer_mobile = models.CharField(max_length=11, default='', verbose_name='签收人电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收货地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.signer_name
