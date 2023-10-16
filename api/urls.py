from django.urls import path

import api.views
from . import views


urlpatterns = [
    path('categories/', views.list_categories),
    path('categories/<int:id>/', views.detail_categories),
    path('products/', api.views.list_products),
    path('products/<int:id>/', api.views.detail_products),
]