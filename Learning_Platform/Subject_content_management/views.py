from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SubjectContent, Subject
from .serializers import SubjectContentSerializer, SubjectSerializer

class SubjectContentViewSet(viewsets.ModelViewSet):
    queryset = SubjectContent.objects.all()
    serializer_class = SubjectContentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]