from django.shortcuts import render
from django.core.serializers import serialize
from django.views.static import serve
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins

from blog.models import Blog
# from .serializers import BlogSerializers
def blog_views(request):
    return render(request, 'blog.html', {})

