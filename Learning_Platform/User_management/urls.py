from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProfileViewSet, login_view, logout_view, register_view, user_home, admin_home, landing_page_view

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user_home/', user_home, name='user_home'),
    path('admin_home/', admin_home, name='admin_home'),
    path('landing_page/', landing_page_view, name='landing_page'),
    
    
]