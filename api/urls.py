
from django.urls import path, include

# from api.region.urls import routers

urlpatterns = [
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('blog/', include('api.Blog.urls')),
    path('region/', include('api.region.urls')),
]