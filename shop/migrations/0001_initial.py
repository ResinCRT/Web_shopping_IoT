# Generated by Django 3.1 on 2020-09-21 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=45, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(blank=True, max_length=45, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=45, null=True)),
                ('read_cnt', models.IntegerField(blank=True, default=0, null=True)),
                ('p_created_dt', models.DateTimeField(blank=True, null=True)),
                ('p_modify_dt', models.DateTimeField(blank=True, null=True)),
                ('brand', models.CharField(max_length=45)),
                ('p_url', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category', verbose_name='Category')),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('content', tinymce.models.HTMLField(verbose_name='CONTENT')),
                ('file', models.CharField(blank=True, max_length=45, null=True)),
                ('r_created_dt', models.DateTimeField(auto_now_add=True)),
                ('r_modify_dt', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USER')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'db_table': 'review',
                'ordering': ('-r_created_dt',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewAttachFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='파일')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
                ('content_type', models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')),
                ('size', models.IntegerField(verbose_name='파일 크기')),
                ('review', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='shop.review', verbose_name='Review')),
            ],
        ),
        migrations.CreateModel(
            name='Qna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qna_title', models.CharField(max_length=50, verbose_name='TITLE')),
                ('content', tinymce.models.HTMLField(verbose_name='CONTENT')),
                ('qna_create_date', models.DateTimeField(auto_now_add=True)),
                ('qna_modify_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USER')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='shop.qna')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'db_table': 'qna',
                'ordering': ('-qna_create_date',),
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductAttachFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='파일')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
                ('content_type', models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')),
                ('size', models.IntegerField(verbose_name='파일 크기')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='shop.product', verbose_name='Post')),
            ],
        ),
    ]
