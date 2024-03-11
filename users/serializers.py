from rest_framework import serializers
from .models import UserUN

class UserunSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUN
        fields = '__all__'
        lookup_fields = 'phone'