from django.urls import path, include

urlpatterns = [
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('blog/', include('api.blog.urls')),
    path('region/', include('api.region.urls')),
]