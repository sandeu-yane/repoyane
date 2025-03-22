from rest_framework import serializers
from .models import EmploiDeTemp

class EmploiDeTempSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploiDeTemp
        fields = '__all__'
