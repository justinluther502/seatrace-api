from .models import Rower
from rest_framework import serializers


class RowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rower
        fields = ['first_name', 'last_name', 'height_ft', 'height_in']
