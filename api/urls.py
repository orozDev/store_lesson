from django.urls import path

import api.views
from . import views


urlpatterns = [
    path('categories/', views.list_categories),
    path('categories/create/', views.create_category),
    path('categories/<int:id>/', views.detail_categories),
    path('categories/<int:id>/update/', views.update_category),
    path('products/', api.views.list_products),
    path('products/create/', api.views.create_product),
    path('products/<int:id>/', api.views.detail_products),
    path('products/<int:id>/update/', api.views.update_product),
]