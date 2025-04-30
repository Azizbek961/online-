from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import get_list_ctg, detail_ctg, ProductView, ProductViews, ProductGenericAPIView, \
    ProductGenericDetailAPIView, ProductGenericAPIViewMixin, ProductGenericDetailAPIViewMixin
from ..region.views import ProductViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet)



urlpatterns = [
    path('', get_list_ctg, name='category-list'),
    path('<int:pk>/', detail_ctg, name='detail-ctg'),
    path("prd/", ProductView.as_view(), name='ctg-id-cls'),
    path('prd/<int:pk>/', ProductViews.as_view(), name='ctg-list-cls'),
    path("generic/", ProductGenericAPIView.as_view()),
    path("generic/<int:pk>/", ProductGenericDetailAPIView.as_view()),
    path("generic/mix/", ProductGenericAPIViewMixin.as_view()),
    path("generic/mix/<int:pk>/", ProductGenericDetailAPIViewMixin.as_view()),
    path("set/", include(router.urls))
]