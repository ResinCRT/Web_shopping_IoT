from django.db import models
# Create your models here.

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    read_cnt = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField('CREATE DATE',auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE')


    class Meta:
        managed = False
        db_table = 'product'