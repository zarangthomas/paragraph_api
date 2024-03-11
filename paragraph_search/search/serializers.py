# search/serializers.py
from rest_framework import serializers
from .models import Paragraph
from rest_framework import generics
class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'text', 'user']  # Adjust the fields you want to include
