from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectContentViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'subject-contents', SubjectContentViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]