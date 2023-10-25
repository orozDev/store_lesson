from django.urls import path, include

import api.views
from . import views


urlpatterns = [
    path('categories/', views.CategoriesGenericAPIView.as_view()),
    path('categories/<int:id>/', views.DetailCategoryGenericAPIView.as_view()),
    path('products/', api.views.list_products),
    path('products/create/', api.views.create_product),
    path('products/<int:id>/', api.views.detail_products),
    path('products/<int:id>/update/', api.views.update_product),
    path('products/<int:id>/delete/', api.views.delete_product),
    path('auth/', include('api.auth.urls')),
]