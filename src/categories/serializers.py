from rest_framework import serializers
from categories.models import Category

#Category Seriliazer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
