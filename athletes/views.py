from .models import Rower, Hull, Race
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from athletes.serializers import RowerSerializer, HullSerializer, RaceSerializer
from trueskill import Rating
from ranking.ranking import race_update, save_mmr


class RowerViewSet(viewsets.ModelViewSet):
    queryset = Rower.objects.all().order_by('last_name')
    serializer_class = RowerSerializer
    permission_classes = [permissions.AllowAny]


class HullViewSet(viewsets.ModelViewSet):
    queryset = Hull.objects.all().order_by('make')
    serializer_class = HullSerializer
    permission_classes = [permissions.AllowAny]


class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all().order_by('date')
    serializer_class = RaceSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        serializer = RaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            winners = serializer.data['winner_crew']
            winner_objs = []
            for winner in winners:
                obj = Rower.objects.get(id=winner['id'])
                obj.old_rating = Rating(mu=obj.mmr, sigma=obj.mmr_uncertainty)
                winner_objs.append(obj)

            losers = serializer.data['loser_crew']
            loser_objs = []
            for loser in losers:
                obj = Rower.objects.get(id=loser['id'])
                obj.old_rating = Rating(mu=obj.mmr, sigma=obj.mmr_uncertainty)
                loser_objs.append(obj)

            winner_old_ratings = [obj.old_rating for obj in winner_objs]
            loser_old_ratings = [obj.old_rating for obj in loser_objs]
            new_win_ratings, new_lose_ratings = race_update(
                winner_old_ratings, loser_old_ratings)

            winner_keys = [obj.id for obj in winner_objs]
            loser_keys = [obj.id for obj in loser_objs]

            save_mmr(winner_keys, tuple(new_win_ratings))
            save_mmr(loser_keys, tuple(new_lose_ratings))

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
