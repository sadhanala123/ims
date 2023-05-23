from django.urls import path

from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('home/', views.home, name='home'),
    path('customer/', views.Customer, name='customer'),
    path('category/', views.Category, name='category'),
    path('brand/', views.Brand, name='brand'),
    path('supplier/', views.Supplier, name='supplier'),
    path('product/',views.Product, name='product'),
    path('purchase/',views.purchase, name='purchase'),
    path('orders/',views.Orders, name='orders'),
    path('del/<int:pk>', views.delete_customer, name='delete'),
    path('del2/<int:pk>', views.delete_category, name='delete2'),
    path('del3/<int:pk>', views.delete_brand, name='delete3'),
    path('del4/<int:pk>', views.delete_product, name='delete4'),
    path('del5/<int:pk>', views.delete_purchase, name='delete5'),
    path('del6/<int:pk>', views.delete_orders, name='delete6'),
    path('del7/<int:pk>', views.delete_supplier, name='delete7'),
    path('update1/<int:pk>',views.update_customer,name='update1'),

]
