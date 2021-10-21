from .models import Rower, Hull, Race
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class RowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rower
        fields = ['first_name', 'last_name', 'height_ft', 'height_in', 'id',
                  'mmr', 'mmr_uncertainty']


class HullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hull
        fields = ['make', 'size', 'year', 'id']


class RaceSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Race
        fields = ['date', 'winner_hull', 'loser_hull', 'winner_crew',
                  'loser_crew', 'draw', 'id']
    winner_hull = HullSerializer(many=False)
    loser_hull = HullSerializer(many=False)
    winner_crew = RowerSerializer(many=True)
    loser_crew = RowerSerializer(many=True)


