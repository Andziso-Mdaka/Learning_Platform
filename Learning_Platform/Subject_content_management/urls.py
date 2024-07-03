# subject_content/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectContentViewSet  # Ensure the correct name is used here

router = DefaultRouter()
router.register(r'subjectcontent', SubjectContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
