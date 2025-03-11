from django.shortcuts import render
from category.models import *
def main(request):
    gb = Category.objects.all()
    return render(request, 'index-2.html',{'gb': gb})
def maind(request):
    gb = Category.objects.all()
    return render(request, 'index-3.html',{'gb': gb})