from .models import Rower
from rest_framework import viewsets
from rest_framework import permissions
from athletes.serializers import RowerSerializer


class RowerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rower.objects.all().order_by('last_name')
    serializer_class = RowerSerializer
    permission_classes = [permissions.AllowAny]
