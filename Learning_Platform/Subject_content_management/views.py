# subject_content/views.py
from rest_framework import viewsets
from .models import SubjectContent  # Ensure the correct name is used here
from .serializers import SubjectContentSerializer

class SubjectContentViewSet(viewsets.ModelViewSet):
    queryset = SubjectContent.objects.all()
    serializer_class = SubjectContentSerializer
