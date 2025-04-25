from django.shortcuts import render
from django.db.models import Prefetch, Count
from django.core.paginator import Paginator
from .models import Product, ProductImage, Category
from category.models import *



def product_list(request):
    page = request.GET.get('page', 1)
    print('PAGE', page)
    products = Product.objects.prefetch_related(Prefetch('images',
            queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
    paginator = Paginator(products, 2)
    page_obj = paginator.get_page(page)
    ctg = Category.objects.all()
    ctgs =  Category.objects.all().annotate(nm=Count('product')).values('name','nm')
    loc = Region.objects.all()
    ctx = {
        "products": products,
        "page_obj": page_obj,
        'count': paginator.count,
        'categories':ctg,
        'ctg':ctgs
    }
    return render(request, 'products.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    image = product.images.all()
    prd_count = Category.objects.annotate(prd_c=Count("product__id"))
    ctg =  Category.objects.all().annotate(nm=Count('product')).values('name','nm')
    ctx = {
        'product': product,
        'images': image,
        "prd_count": prd_count,
        'ctg':ctg
    }
    return render(request, 'detail.html', ctx)


