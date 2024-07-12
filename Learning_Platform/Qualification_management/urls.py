# qualifications/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QualificationViewSet

router = DefaultRouter()
router.register(r'qualifications', QualificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
