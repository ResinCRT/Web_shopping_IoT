from django.db import models
from shop.models import Product
from register.models import User

# from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    order_dt = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'order'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True)
    product = models.ForeignKey(Product, models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'order_detail'

    def sub_total(self):
        # 템플릿에서 사용하는 변수로 주문내역에 담긴 각 상품의 합계
        return self.product.price * self.quantity
