from rest_framework import viewsets
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]  # Ensure this viewset is accessible to everyone

    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
