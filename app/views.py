from django.shortcuts import get_object_or_404, render

from .models import Category, Product, ProductInShop


def index(request):
    categories_list = Category.objects.order_by('-created')
    context = {
        'categories_list': categories_list,
    }
    return render(request, 'app/index.html', context=context)


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category,
    }
    return render(request, 'app/category.html', context=context)


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_in_shops = ProductInShop.objects.filter(product=product)
    context = {
        'product': product,
        'product_in_shops': product_in_shops,
    }
    return render(request, 'app/product.html', context=context)
