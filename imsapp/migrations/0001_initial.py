# Generated by Django 4.1.7 on 2023-04-24 12:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ims_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ims_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ims_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('mobile', models.IntegerField(default=0)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Ims_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(default=True, max_length=300)),
                ('model', models.CharField(default=True, max_length=250)),
                ('description', models.TextField()),
                ('quantity', models.CharField(default=True, max_length=200)),
                ('unit', models.CharField(default=True, max_length=150)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minimum_order', models.DecimalField(decimal_places=2, max_digits=10)),
                ('suplier', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('brandid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsapp.ims_brand')),
                ('categoryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsapp.ims_category')),
            ],
        ),
        migrations.CreateModel(
            name='Ims_suplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=200)),
                ('mobile', models.IntegerField(default=0)),
                ('address', models.TextField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ims_Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=255)),
                ('purchase_date', models.DateTimeField(default=datetime.datetime.now)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsapp.ims_product')),
                ('suplier_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsapp.ims_suplier')),
            ],
        ),
        migrations.CreateModel(
            name='Ims_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_shipped', models.IntegerField()),
                ('order_date', models.DateTimeField(default=datetime.datetime.now)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsapp.ims_customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsapp.ims_product')),
            ],
        ),
        migrations.AddField(
            model_name='ims_brand',
            name='categoryid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imsapp.ims_category'),
        ),
    ]
