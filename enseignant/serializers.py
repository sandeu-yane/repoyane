from rest_framework import serializers
from .models import Assiduite, Note

class AssiduiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assiduite
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'