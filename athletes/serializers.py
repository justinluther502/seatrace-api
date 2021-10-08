from .models import Rower, Hull, Boat
from rest_framework import serializers


class RowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rower
        fields = ['first_name', 'last_name', 'height_ft', 'height_in', 'id',
                  'mmr', 'mmr_uncertainty']


class HullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hull
        fields = ['make', 'size', 'year', 'id']


class BoatSerializer(serializers.ModelSerializer):
    hull = HullSerializer(many=False, read_only=True)
    crewmembers = RowerSerializer(many=True, read_only=True)
    class Meta:
        model = Boat
        fields = ['date', 'hull', 'crewmembers', 'id']
