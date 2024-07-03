# qualifications/views.py
from rest_framework import viewsets
from .models import Qualification
from .serializers import QualificationSerializer

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
