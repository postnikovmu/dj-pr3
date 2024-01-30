from rest_framework import serializers
from .models import Good


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(required=False)


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('name', 'amount', 'price',)
