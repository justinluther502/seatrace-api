from .models import Rower, Hull, Race
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
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

    def create(self, request):
        serializer = RaceSerializer(data=request.data)
        if serializer.is_valid():
            # TODO: put MMR update stuff here.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
