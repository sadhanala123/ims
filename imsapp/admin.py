# from django.contrib import admin
# from .models import Ims_customer
# from .models import Ims_category, Ims_brand
# from .models import Ims_product
# from .models import Ims_suplier
# from .models import Ims_Purchase
# from .models import Ims_order
#
#
#
# # Register your models here.
# class  Ims_customerAdmin(admin.ModelAdmin):
#        list_display = ('id', 'name', 'address', 'mobile', 'balance',)
#        list_display_links = ('id', 'name',)
#        list_filter = ('name',)
#        list_editable = ('mobile',)
#        search_fields = ('name',)
#        ordering = ('name',)
#
# admin.site.register(Ims_customer,Ims_customerAdmin)
# class  Ims_categoryAdmin(admin.ModelAdmin):
#        list_display = ('id', 'name', 'status',)
#        list_display_links = ('id', 'name',)
#
# admin.site.register(Ims_category,Ims_categoryAdmin)
#
# class Ims_brandAdmin(admin.ModelAdmin):
#        list_display = ('id','bname','categoryid','status',)
# admin.site.register(Ims_brand,Ims_brandAdmin)
#
# class Ims_suplierAdmin(admin.ModelAdmin):
#        list_display = ('id','sname','mobile','address','status',)
#
# admin.site.register(Ims_suplier,Ims_suplierAdmin)
#
# class Ims_productAdmin(admin.ModelAdmin):
#        list_display = ('id','pname','categoryid','brandid','model','description','quantity','unit','base_price','tax','minimum_order','suplier','status','date',)
#
# admin.site.register(Ims_product,Ims_productAdmin )
# class Ims_PurchaseAdmin(admin.ModelAdmin):
#        list_display = ('id','suplier_id','product_id','quantity','purchase_date',)
#
# admin.site.register(Ims_Purchase,Ims_PurchaseAdmin)
#
# class Ims_orderAdmin(admin.ModelAdmin):
#        list_display = ('id','product_id','total_shipped','customer_id','order_date',)
#
# admin.site.register(Ims_order,Ims_orderAdmin)

from django.contrib import admin

# Register your models here.
from .models import Add_customer
from .models import Add_category
# from .models import Brand_category
from .models import Add_brand
from .models import Add_supplier
from .models import Add_product
from .models import Add_purchase
from .models import Add_orders


admin.site.register(Add_customer)
admin.site.register(Add_category)
# admin.site.register(Brand_category)


admin.site.register(Add_brand)
admin.site.register(Add_supplier)
admin.site.register(Add_product)
admin.site.register(Add_purchase)
admin.site.register(Add_orders)

