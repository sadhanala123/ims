# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth




from .models import Add_customer
from .models import Add_category
# from .models import Brand_category
from .models import Add_brand
from .models import Add_supplier
from .models import Add_product
from .models import Add_purchase
from .models import Add_orders


from .forms import Add_brandForm
from .forms import Add_ordersForm
from .forms import Add_productForm
from .forms import Add_purchaseForm

# Create your views here.
# from .forms import Add_customerForm


def home(request):
    return render(request, 'home.html')


def Customer(request):
    display = Add_customer.objects.all()
    #
    if request.method == 'POST':
        name6 = request.POST.get("name")
        phone1 = request.POST.get("phone")
        balance1 = request.POST.get("balance")
        address1 = request.POST.get("address")
        data = Add_customer(Name=name6, mobile=phone1, balance=balance1, Address=address1)
        data.save()
    context = {'display': display}

    return render(request, 'customerManagement.html', context)


def Category(request):
    display_category = Add_category.objects.all()

    if request.method == 'POST':
        name1 = request.POST.get("name")
        # status1 = request.POST.get("status")
        data = Add_category(Category_name=name1)
        data.save()
    context = {'display_category': display_category}
    return render(request, 'category.html', context)


def Brand(request):
    display_brand = Add_brand.objects.all()
    # display_brand_category = Brand_category
    form = Add_brandForm()
    #
    if request.method == 'POST':
            form = Add_brandForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('brand')
        # name2 = request.POST.get("name")
        # name1 = request.POST.get("dropdown")
        # # status1 = request.POST.get("status")
        # data = Add_brand(brand_name=name2, Category_name=name1)
        # data.save()
    context = {'display_brand': display_brand,
               'form': form}

    return render(request, 'Brand.html', context)


def Supplier(request):
    display_supplier = Add_supplier.objects.all()

    if request.method == 'POST':
        name4 = request.POST.get("name")
        phone1 = request.POST.get("phone")
        address1 = request.POST.get("address")
        data = Add_supplier(supplier_name=name4, mobile=phone1, Address=address1)
        data.save()

    context = {'display_supplier': display_supplier}
    return render(request, 'suplier.html', context)


def Product(request):
    display_product = Add_product.objects.all()
    form = Add_productForm()

    if request.method == 'POST':
        form = Add_productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')

        # name1 = request.POST.get("category")
        # name2 = request.POST.get("brand")
        # name3 = request.POST.get("name")
        # model1 = request.POST.get("model")
        # description1 = request.POST.get("description")
        # quantity1 = request.POST.get("quantity")
        # price1 = request.POST.get("base price")
        # tax1 = request.POST.get("tax")
        # name4 = request.POST.get("supplier name")
        # data = Add_product(Category_name=name1, brand_name=name2, product_name=name3, product_model=model1,
        #                    product_description=description1, product_quantity=quantity1, product_base_price=price1,
        #                    product_tax=tax1, supplier_name=name4)
        # data.save()

    context = {'display_product': display_product,
               'form': form}
    return render(request, 'Product.html', context)


def purchase(request):
    display_purchase = Add_purchase.objects.all()
    form = Add_purchaseForm()

    if request.method == "POST":
        form = Add_purchaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('purchase')
        # name1 = request.POST.get("name")
        # quantity1 = request.POST.get("quantity")
        # name4 = request.POST.get("supplier")
        # data = Add_purchase(product_name=name1, product_quantity=quantity1, supplier_name=name4)
        # data.save()

    context = {'display_purchase': display_purchase,
               'form': form}
    return render(request, 'purchase.html', context)


def Orders(request):
    display_orders = Add_orders.objects.all()
    form = Add_ordersForm()

    if request.method == "POST":
        form = Add_ordersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('orders')

        # name3 = request.POST.get("name")
        # item1 = request.POST.get("item")
        # name6 = request.POST.get("name1")
        # data = Add_orders(product_name=name3, total_item=item1, Name=name6)
        # data.save()
    context = {'display_orders': display_orders,
               'form': form}
    return render(request, 'order.html', context)

def delete_customer(request, pk):
    delete1 = Add_customer.objects.get(id=pk)
    delete1.delete()

    return redirect('customer')

def delete_category(request, pk):
    delete2 = Add_category.objects.get(id=pk)
    delete2.delete()

    return redirect('category')

def delete_brand(request, pk):
    delete3 = Add_brand.objects.get(id=pk)
    delete3.delete()

    return redirect('brand')

def delete_product(request, pk):
    delete4 = Add_product.objects.get(id=pk)
    delete4.delete()

    return redirect('product')

def delete_purchase(request, pk):
    delete5 = Add_purchase.objects.get(id=pk)
    delete5.delete()

    return redirect('purchase')

def delete_orders(request, pk):
    delete6 = Add_orders.objects.get(id=pk)
    delete6.delete()

    return redirect('orders')

def delete_supplier(request, pk):
    delete7 = Add_supplier.objects.get(id=pk)
    delete7.delete()

    return redirect('supplier')




def Login(request):
    if request.method == 'POST':  # (POST=POST)true
        username = request.POST['username']  # raja(geting data from login page <input type='username' name='username)
        password = request.POST[
            'password']  # Welcome@123(geting data from login page <input type='password' name='password)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login Successfully')
            return redirect('home')
        else:
            print('You Provided Invalid Credintials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def update_customer(request, pk):
   update1 = Add_customer.objects.get(id=pk)
   update1.update1()
   return redirect('customer')

def update_category(request, pk):
    delete2 = Add_category.objects.get(id=pk)
    delete2.delete()

    return redirect('category')

def update_brand(request, pk):
    delete3 = Add_brand.objects.get(id=pk)
    delete3.delete()

    return redirect('brand')

def delete_product(request, pk):
    delete4 = Add_product.objects.get(id=pk)
    delete4.delete()

    return redirect('product')

def delete_purchase(request, pk):
    delete5 = Add_purchase.objects.get(id=pk)
    delete5.delete()

    return redirect('purchase')

def delete_orders(request, pk):
    delete6 = Add_orders.objects.get(id=pk)
    delete6.delete()

    return redirect('orders')

def delete_supplier(request, pk):
    delete7 = Add_supplier.objects.get(id=pk)
    delete7.delete()

    return redirect('supplier')