from .models import Rower, Hull, Race
from rest_framework import viewsets
from rest_framework import permissions
from athletes.serializers import RowerSerializer, HullSerializer, RaceSerializer


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

    # def create(self, request):
    #     # Use online docs to make writeable nested serializer.
    #     pass
