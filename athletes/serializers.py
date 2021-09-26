from .models import Rower, Hull, Boat
from rest_framework import serializers


class RowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rower
        fields = ['first_name', 'last_name', 'height_ft', 'height_in', 'id']


class HullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hull
        fields = ['make', 'size', 'year', 'id']


class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = ['date', 'hull', 'crewmember', 'id']
