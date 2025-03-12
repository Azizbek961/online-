from django.urls import path
from .views import *
urlpatterns = [
    path('', main),
    path('index-2.html', main),
    path('index-3.html', maind),
    path('category.html', mains),
    path('adlistinglist.html', mainq),
    path('adlistinggrid.html', mainw),
    path('ads-details.html', maine),

]

