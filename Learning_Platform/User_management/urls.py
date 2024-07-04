
# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


# profiles/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet
from .views import login_view
from .views import login_view, user_home

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
       path('login/', login_view, name='login'),
    path('home/', user_home, name='user_home'),
      
    
]
