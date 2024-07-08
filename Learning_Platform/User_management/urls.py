# user_management/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

# user_management/urls.py

from django.urls import path
from .views import login_view, logout_view, user_home, admin_home,register_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_home/', admin_home, name='admin_home'),
    path('user_home/', user_home, name='user_home'),
    path('register/', register_view, name='register'),
    
    

]