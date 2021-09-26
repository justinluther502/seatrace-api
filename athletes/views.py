from .models import Rower, Hull, Boat
from rest_framework import viewsets
from rest_framework import permissions
from athletes.serializers import RowerSerializer, HullSerializer, BoatSerializer


class RowerViewSet(viewsets.ModelViewSet):
    queryset = Rower.objects.all().order_by('last_name')
    serializer_class = RowerSerializer
    permission_classes = [permissions.AllowAny]


class HullViewSet(viewsets.ModelViewSet):
    queryset = Hull.objects.all().order_by('make')
    serializer_class = HullSerializer
    permission_classes = [permissions.AllowAny]


class BoatViewSet(viewsets.ModelViewSet):
    queryset = Boat.objects.all().order_by('date')
    serializer_class = BoatSerializer
    permission_classes = [permissions.AllowAny]