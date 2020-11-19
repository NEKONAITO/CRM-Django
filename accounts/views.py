from .models import *
from django.shortcuts import render, redirect
from .forms import OrderForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Entregado').count()
    pending = orders.filter(status='Pendiente').count()

    context = {'orders':orders, 'customers':customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    context = {'products':products}
    return render(request, 'accounts/products.html', context)

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    customer_order = customer.order_set.all()
    order_count = customer_order.count()

    myFilter = OrderFilter(request.GET, queryset=customer_order)
    customer_order = myFilter.qs

    context = {'customer':customer, 'customer_order':customer_order, 'order_count':order_count, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)

# CRUD --------------------------------------------------------

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'form':formset}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)