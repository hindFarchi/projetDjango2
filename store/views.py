from django.shortcuts import get_object_or_404, render, redirect

from .models import Category, Product
from .forms import ProductFrom


def product_crud(request, id=0):
    if request.user.is_authenticated and request.user.is_superuser:
        if id == 0:
            form = ProductFrom(request.POST or None)
        else:
            if request.method == 'GET':
                form = ProductFrom(instance=Product.objects.get(id=id))
            else:
                form = ProductFrom(request.POST, instance=Product.objects.get(id=id))
            products = Product.objects.all()
            context = {'products': products, 'form': form}
        if form.is_valid():
            form.save()
            form = ProductFrom()
        products = Product.objects.all()
        messages = form.errors
        context = {'products': products, 'form': form, 'messages': messages}
        return render(request, 'store/product_crud.html', context)
    else:
        return redirect('/login/login')


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/home.html', {'products': products})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    if product is None:
        return redirect('/')
    return render(request, 'store/products/single.html', {'product': product})


def delete_product(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/product_crud')
