# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cart(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    product_id = models.ForeignKey('Product_id', models.DO_NOTHING, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cart'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=45, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Inventory(models.Model):
    product_id = models.ForeignKey('Product_id', models.DO_NOTHING)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory'


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('User_id', models.DO_NOTHING, blank=True, null=True)
    product_id = models.ForeignKey('Product_id', models.DO_NOTHING, blank=True, null=True)
    wish_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


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
        unique_together = (('product_id', 'category_category_id'),)


class Qna(models.Model):
    qna_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=45, blank=True, null=True)
    qna_create_date = models.DateTimeField(blank=True, null=True)
    qna_modify_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qna'


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('User_id', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=45, blank=True, null=True)
    file = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


