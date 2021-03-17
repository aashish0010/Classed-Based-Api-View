from rest_framework import serializers
from .models import Home


class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField()
        model = Home
        fields = ['id','username', 'email', 'password']