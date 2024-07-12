from rest_framework import serializers
from .models import SubjectContent, Subject

class SubjectContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectContent
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'