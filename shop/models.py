from django.db import models
# from django.contrib.auth.models import User
from register.models import User
from django.urls import reverse
from tinymce.models import HTMLField


class Product(models.Model):
    p_name = models.CharField(max_length=45, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=45, blank=True, null=True)
    read_cnt = models.IntegerField(blank=True, null=True, default=0)
    category_id = models.IntegerField(blank=True, null=True)
    p_created_dt = models.DateTimeField(blank=True,null=True)
    p_modify_dt = models.DateTimeField(blank=True, null=True)
    brand = models.CharField(max_length=45)
    p_url = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'product'

    def __str__(self):
        return self.p_name

    def get_absolute_url(self):  # 현재 데이터의 절대 경로 추출
        # 경로변수인 슬러그의 값을 args로 받는다
        return reverse('shop:detail', args=(self.id,))

    def get_previous(self):  # 이전 데이터 추출
        return self.get_previous_by_modify_dt()

    def get_next(self):  # 다음 데이터 추출
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Qna(models.Model):
    qna_title = models.CharField(verbose_name='TITLE', max_length=50)
    product = models.ForeignKey(Product, models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    parent = models.ForeignKey('self', related_name='replies', on_delete=models.CASCADE, null=True, blank=True)
    # content = models.TextField()
    content = HTMLField('CONTENT')
    qna_create_date = models.DateTimeField(auto_now_add=True)
    qna_modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'qna'

    def __str__(self):
        return self.content


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='USER', blank=True)
    review_title = models.CharField(verbose_name='TITLE', max_length=50)
    product = models.ForeignKey(Product, models.CASCADE, blank=True, null=True)
    rating = models.IntegerField()
    content = models.CharField(max_length=45)
    file = models.CharField(max_length=45, blank=True, null=True)
    r_created_dt = models.DateTimeField(auto_now_add=True)
    r_modify_dt = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'review'

    def __str__(self):
        return self.review_title


class Category(models.Model):
    category_name = models.CharField(max_length=45, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'category'


class ProductAttachFile(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="files", verbose_name='Post', blank=True, null=True)
    upload_file = models.FileField(upload_to="%Y/%m/%d", null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    content_type = models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')
    size = models.IntegerField('파일 크기')

    def __str__(self):
        return self.filename


class ReviewAttachFile(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="files", verbose_name='Review', blank=True, null=True)
    upload_file = models.ImageField(upload_to="%Y/%m/%d", null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    content_type = models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')
    size = models.IntegerField('파일 크기')

    def __str__(self):
        return self.filename

class Wishlist(models.Model):
    pass