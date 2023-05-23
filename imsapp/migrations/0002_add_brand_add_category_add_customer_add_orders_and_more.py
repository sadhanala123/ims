# Generated by Django 4.2.1 on 2023-05-23 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=200)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=200)),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=12)),
                ('balance', models.CharField(max_length=10)),
                ('Address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Add_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_item', models.IntegerField()),
                ('Name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imsapp.add_customer')),
            ],
        ),
        migrations.CreateModel(
            name='Add_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_model', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('product_quantity', models.IntegerField()),
                ('product_base_price', models.CharField(max_length=5)),
                ('product_tax', models.CharField(max_length=5)),
                ('status', models.BooleanField(default=True)),
                ('Category_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imsapp.add_category')),
                ('brand_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imsapp.add_brand')),
            ],
        ),
        migrations.CreateModel(
            name='Add_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField()),
                ('product_name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imsapp.add_product')),
            ],
        ),
        migrations.CreateModel(
            name='Add_supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=12)),
                ('Address', models.TextField()),
                ('Status', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ims_order',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='ims_order',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='ims_product',
            name='brandid',
        ),
        migrations.RemoveField(
            model_name='ims_product',
            name='categoryid',
        ),
        migrations.RemoveField(
            model_name='ims_purchase',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='ims_purchase',
            name='suplier_id',
        ),
        migrations.DeleteModel(
            name='Ims_brand',
        ),
        migrations.DeleteModel(
            name='Ims_category',
        ),
        migrations.DeleteModel(
            name='Ims_customer',
        ),
        migrations.DeleteModel(
            name='Ims_order',
        ),
        migrations.DeleteModel(
            name='Ims_product',
        ),
        migrations.DeleteModel(
            name='Ims_Purchase',
        ),
        migrations.DeleteModel(
            name='Ims_suplier',
        ),
        migrations.AddField(
            model_name='add_purchase',
            name='supplier_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imsapp.add_supplier'),
        ),
        migrations.AddField(
            model_name='add_product',
            name='supplier_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imsapp.add_supplier'),
        ),
        migrations.AddField(
            model_name='add_orders',
            name='product_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imsapp.add_product'),
        ),
        migrations.AddField(
            model_name='add_brand',
            name='Category_name',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='imsapp.add_category'),
        ),
    ]