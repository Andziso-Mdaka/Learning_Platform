# qualifications/serializers.py

from rest_framework import serializers
from .models import Qualification
from Student_Management.serializers import SubjectSerializer

class QualificationSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = Qualification
        fields = ['id', 'name', 'description', 'created_at', 'subjects']
