from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    read_cnt = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    product_id = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Qna(models.Model):
    qna_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    parent_id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=45, blank=True, null=True)
    qna_create_date = models.DateTimeField(blank=True, null=True)
    qna_modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qna'


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=45, blank=True, null=True)
    file = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    product_id = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    wish_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


class Inventory(models.Model):
    product_id = models.ForeignKey('Product', models.DO_NOTHING)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=45, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

