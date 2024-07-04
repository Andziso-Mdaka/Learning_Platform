# user_management/urls.py

from django.urls import path, include
from .views import login_view, register_view, landing_page_view, user_home, admin_home
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', landing_page_view, name='landing_page'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('user_home/', user_home, name='user_home'),
    path('admin_home/', admin_home, name='admin_home'),
    path('api/', include(router.urls)),
]
