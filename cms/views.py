from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}
    return render(request, 'cms/dashboard.html', context)


def products(request):
    products = Product.objects.all()

    return render(request, 'cms/products.html', {'products': products})


def customer(request):
    return render(request, 'cms/customer.html')