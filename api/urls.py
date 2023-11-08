from django.urls import path, include

import api.views
from . import views

from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as url_doc

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('products-image', views.ProductImageViewSet)
router.register('products-attribute', views.ProductAttributeViewSet)
router.register('categories', views.CategoryViewSet)
router.register('tags', views.TagViewSet)


urlpatterns = [
    path('auth/', include('api.auth.urls')),

    path('', include(router.urls))
]

urlpatterns += url_doc