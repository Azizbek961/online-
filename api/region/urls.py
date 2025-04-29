# from django.urls import path, include
# from .views import get_list_rgn, detail_rgn, RegionGenericAPIView, RegionGenericDetailAPIView, \
#     RegionGenericAPIViewMixin, RegionGenericDetailAPIViewMixin, ProductViewSet
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'', ProductViewSet)
#
# urlpatterns = [
#     path("", get_list_rgn, name='region-list'),
#     path("<int:pk>/", detail_rgn, name='detail-rgn'),
#     path("generic/", RegionGenericAPIView.as_view()),
#     path("generic/<int:pk>/", RegionGenericDetailAPIView.as_view()),
#     path("generic/mix/", RegionGenericAPIViewMixin.as_view()),
#     path("generic/mix/<int:pk>/", RegionGenericDetailAPIViewMixin.as_view()),
#     path("set/", include(router.urls))
# ]