from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from category.models import Category,Region
from product.models import Product, ProductImage
from .forms import LoginForm,ProductForm
# from .models import Region

def contact(request):
    return redirect('main')
def main(request):
    categories = Category.objects.filter(is_main=True)
    region = Region.objects.all()
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images')
    )

    context = {
        "categories": categories,
        "products": products,
        "a": 1234567890,
        "region": region
    }

    return render(request, 'index.html', context)


def login_view(request):
    form = LoginForm()
    Url = request.GET.get('url','main')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(Url)
            else:
                form.add_error(None, "Login yoki parol noto‘g‘ri")

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main')


def main_page(request):
    for_header = Category.objects.filter(for_header=True)
    for_footer = Category.objects.filter(for_footer=True)
    for_mid_part = Category.objects.filter(for_mid_part=True)
    is_option = Category.objects.filter(is_option=True)

    products = Category.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_image')
    )

    location = Region.objects.all()

    context = {
        'for_header': for_header,
        'for_footer': for_footer,
        'for_mid_part': for_mid_part,
        'is_option': is_option,
        'products': products,
        'location': location,
    }

    return render(request, 'main.html', context)
def post_add(request):
    post = ProductForm()
    if request.method == "POST":
        post = ProductForm(request.POST)
        print(post,post.is_valid())
        if post.is_valid():
            prod = post.save(commit=False)
            prod.user = request.user.profile
            prod.save()
            return redirect('main')
        else:
            post.add_error(None,'Field larin toliq toldiring')
    else:
        post = ProductForm()
    ctx = {
        'form':post
    }
    return render(request,'post_add.html',ctx)