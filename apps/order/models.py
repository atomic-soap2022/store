from django.db import models

from apps.catalog.models import Product
from apps.user.models import User
from apps.main.mixins import MetaTagMixin


class Cart(MetaTagMixin):
    product = models.ForeignKey(to=Product, verbose_name='Продукт', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество')
    user = models.ForeignKey(to=User, verbose_name='Покупатель', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
