# app/urls.py
from django.urls import path
from .views import MyTokenObtainPairView, SecureView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('secure/', SecureView.as_view(), name='secure_view'),
]
