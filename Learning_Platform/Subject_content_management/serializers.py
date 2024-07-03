# subject_content/serializers.py
from rest_framework import serializers
from .models import SubjectContent  # Ensure the correct name is used here

class SubjectContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectContent
        fields = '__all__'
