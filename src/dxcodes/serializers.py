from rest_framework import serializers
from dxcodes.models import Dxcode

# Dxcode Serializer
class DxcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dxcode
        fields = '__all__'