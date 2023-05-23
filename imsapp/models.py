# from django.db import models
# from datetime import datetime
# from phone_field import PhoneField
#
# # Create your models here.
# class Ims_customer(models.Model):
#     name=models.CharField(max_length=200,blank=False)
#     address=models.TextField()
#     mobile = models.CharField(max_length=12)
#     balance=models.DecimalField(max_digits=5, decimal_places=2)
# class Ims_category(models.Model):
#     name=models.CharField(max_length=250)
#     status=models.BooleanField(default=True)
#
# class Ims_brand(models.Model):
#     categoryid=models.ForeignKey(Ims_category,on_delete=models.CASCADE,)
#     bname=models.CharField(max_length=250,blank=False)
#     status=models.BooleanField(default=True)
#
# class Ims_suplier(models.Model):
#     sname=models.CharField(max_length=200,blank=False)
#     mobile = models.CharField(max_length=12)
#     address=models.TextField()
#     status=models.BooleanField(default=True)
#
# class Ims_product(models.Model):
#     categoryid=models.ForeignKey(Ims_category,on_delete=models.CASCADE,)
#     brandid=models.ForeignKey(Ims_brand,on_delete=models.CASCADE,)
#     pname=models.CharField(max_length=300,default=True)
#     model=models.CharField(max_length=250,default=True)
#     description=models.TextField()
#     quantity=models.CharField(max_length=200,default=True)
#     unit=models.CharField(max_length=150,default=True)
#     base_price=models.DecimalField(max_digits=10,decimal_places=2)
#     tax=models.DecimalField(max_digits=10,decimal_places=2)
#     minimum_order=models.DecimalField(max_digits=10,decimal_places=2)
#     suplier=models.IntegerField(default=0)
#     status=models.BooleanField(default=True)
#     date=models.DateTimeField(default=datetime.now, blank=True)
#
# class Ims_Purchase(models.Model):
#      suplier_id=models.ForeignKey(Ims_suplier,on_delete=models.CASCADE,)
#      product_id=models.ForeignKey(Ims_product,on_delete=models.CASCADE,)
#      quantity=models.CharField(max_length=255)
#      purchase_date=models.DateTimeField(default=datetime.now)
# class Ims_order(models.Model):
#       product_id=models.ForeignKey(Ims_product,on_delete=models.CASCADE,)
#       total_shipped=models.IntegerField()
#       customer_id=models.ForeignKey(Ims_customer,on_delete=models.CASCADE,)
#       order_date=models.DateTimeField(default=datetime.now,)


# import active as active
from django.db import models


class Add_customer(models.Model):
    Name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=12)
    balance = models.CharField(max_length=10)
    Address = models.TextField()


def __str__(self):
    return self.Name


class Add_category(models.Model):
    Category_name = models.CharField(max_length=200)
    Status = models.BooleanField(default=True)

    def __str__(self):
        return self.Category_name


# class Brand_category(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name


class Add_brand(models.Model):
    brand_name = models.CharField(max_length=200)
    Category_name =  models.ForeignKey(Add_category, on_delete=models.CASCADE, default=True, null=False)
    Status = models.BooleanField(default=True)
    #
    def __str__(self):
        return self.brand_name


# models.ForeignKey(Brand_category, on_delete=models.CASCADE, default=True, null=False)
class Add_supplier(models.Model):
    supplier_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=12)
    Address = models.TextField()
    Status = models.BooleanField(default=True)

    def __str__(self):
        return self.supplier_name
#
class Add_product(models.Model):
    Category_name =  models.ForeignKey(Add_category, on_delete=models.CASCADE, default=True, null=False)
    brand_name =  models.ForeignKey(Add_brand, on_delete=models.CASCADE, default=True, null=False)
    product_name = models.CharField(max_length=200)
    product_model = models.CharField(max_length=200)
    product_description = models.TextField()
    product_quantity = models.IntegerField()
    product_base_price = models.CharField(max_length=5)
    product_tax = models.CharField(max_length=5)
    supplier_name =  models.ForeignKey(Add_supplier, on_delete=models.CASCADE, default=True, null=False)
    status = models.BooleanField(default=True)
    #
    def __str__(self):
        return self.product_name
#
class Add_purchase(models.Model):
    product_name = models.ForeignKey(Add_product, on_delete=models.CASCADE, default=True, null=False)
    product_quantity = models.IntegerField()
    supplier_name =  models.ForeignKey(Add_supplier, on_delete=models.CASCADE, default=True, null=False)

class Add_orders(models.Model):
    product_name = models.ForeignKey(Add_product, on_delete=models.CASCADE, default=True, null=False)
    total_item = models.IntegerField()
    Name = models.ForeignKey(Add_customer, on_delete=models.CASCADE, default=True, null=False)
#
#
