from django.shortcuts import render
from category.models import *


def main(request):
    gb = Category.objects.all()
    return render(request, 'index-2.html', {'gb': gb})


def maind(request):
    gb = Category.objects.all()
    return render(request, 'index-3.html', {'gb': gb})


def mains(request):
    gb = Category.objects.all()
    return render(request, 'category.html', {'gb': gb})

def mainq(request):
    gb = Category.objects.all()
    return render(request, 'adlistinglist.html', {'gb': gb})

def mainw(request):
    gb = Category.objects.all()
    return render(request, 'adlistinggrid.html', {'gb': gb})

def maine(request):
    gb = Category.objects.all()
    return render(request, 'ads-details.html', {'gb': gb})
def product_detail(request, pk):
    return render(request)