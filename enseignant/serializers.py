from rest_framework import serializers
from .models import Assiduite

class AssiduiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assiduite
        fields = '__all__'
