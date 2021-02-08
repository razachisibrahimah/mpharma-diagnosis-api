from dxcodes.models import Dxcode
from rest_framework import viewsets, permissions
from .serializers import DxcodeSerializer

# Dxcode Viewset
class DxcodeViewSet(viewsets.ModelViewSet):
    queryset = Dxcode.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DxcodeSerializer
