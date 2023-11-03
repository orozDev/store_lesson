from django.urls import path, include

import api.views
from . import views

from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as url_doc

router = DefaultRouter()
router.register('products', views.ProductReadOnlyModelViewSet)
router.register('categories', views.CategoryModelViewSet)


urlpatterns = [
    path('products/create/', api.views.create_product),
    path('products/<int:id>/update/', api.views.update_product),
    path('products/<int:id>/delete/', api.views.delete_product),
    path('auth/', include('api.auth.urls')),

    path('', include(router.urls))
]

urlpatterns += url_doc