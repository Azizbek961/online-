from django.urls import path
from .views import main, contact,post_add

urlpatterns = [
    path('', main, name='main'),
    path('contact',contact, name='contact'),
    path('post_add/',post_add,name='post_add'),
]
