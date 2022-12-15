from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required()
def product_add(request):
    template_name = 'products/product_add.html'
    form = ProductAdd()
    context = {'form': form}
    if request.method == "POST":
        form = ProductAdd(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.created_user = str(request.user)
            data.save()
            messages.success(request, 'Product Details Successfully Added.', 'alert-success')
            return redirect('product_list')
        else:
            context = {'form': form}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    return render(request, template_name, context)


@login_required()
def product_list(request):
    template_name = 'products/product_list.html'
    product_list = Products.objects.all()
    context = {'product_list':product_list}
    return render(request, template_name, context)


@login_required()
def product_details(request, pk):
    template_name = 'products/product_details.html'
    products = Products.objects.get(product_id=pk)
    context = {'product':products}
    return render(request, template_name, context)


@login_required()
def product_delete(request, pk):
    Products.objects.get(product_id=pk).delete()
    messages.success(request, 'Product details are deleted..', 'alert-success')
    return redirect('product_list')


@login_required()
def product_edit(request, pk):
    template_name = 'products/product_edit.html'
    product = Products.objects.get(product_id=pk)
    form = ProductAdd(instance=product)
    context = {'form': form, 'product': product}
    if request.method == "POST":
        form = ProductAdd(request.POST, request.FILES, instance=product)
        if form.is_valid():
            data = form.save(commit=False)
            data.updated_user = str(request.user)
            data.updated_at = datetime.now()
            data.save()
            messages.success(request, 'Product Details Successfully Updated.', 'alert-success')
            return redirect('product_list')
        else:
            context = {'form': form}
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    return render(request, template_name, context)