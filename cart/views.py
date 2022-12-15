from django.shortcuts import render, redirect
from products.models import *
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    products = Products.objects.all()
    clothing = Products.objects.filter(product_category="Clothing")
    electronics = Products.objects.filter(product_category="Electronics")
    veg = Products.objects.filter(product_category="Vegetables")
    furniture = Products.objects.filter(product_category="Furniture")
    med = Products.objects.filter(product_category="Medicines")
    context = {'cloths': clothing, 'electronics': electronics, 'veg': veg, 'furniture': furniture, 'med': med,
               'products': products}
    return render(request, 'cart/home.html', context)


def add_to_cart(request, pk):
    user = request.user
    product = Products.objects.get(product_id=pk)
    product_exists = Cart.objects.filter(user=user, product=product).exists()
    if product_exists:
        messages.success(request, f"{product.product_name} already added to cart", 'alert-danger')
        return redirect('home')
    else:
        Cart.objects.create(created_user=request.user, user=user, product=product)
        messages.success(request, f"{product.product_name} added to cart", 'alert-success')
        return redirect('home')


def cart_list(request):
    user = request.user
    products = Cart.objects.filter(user=user)
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, 'cart/cart_list.html', context)


def remove_from_cart(request, pk):
    user = request.user
    product = Products.objects.get(product_id=pk)
    Cart.objects.get(user=user, product=product).delete()
    return redirect('cart_list')

