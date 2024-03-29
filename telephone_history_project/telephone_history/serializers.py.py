from rest_framework import serializers
from .models import TelephoneHistory

class TelephoneHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TelephoneHistory
        fields = ['id', 'name', 'time', 'number']
