from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginGenericAPIView.as_view()),
    path('register/', views.RegisterGenericAPIView.as_view()),
]