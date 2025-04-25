from django.urls import path
from .views import get_list_ctg, detail_ctg, ProductView, ProductViews

urlpatterns = [
    path('', get_list_ctg, name='category-list'),
    path('<int:pk>/', detail_ctg, name='detail-ctg'),
    path("prd/", ProductView.as_view(), name='ctg-id-cls'),
    path('prd/<int:pk>/', ProductViews.as_view(), name='ctg-list-cls')
]