from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from .forms import CategoryForm, ProductForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.product_set.all()
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'shop/add_category.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})
