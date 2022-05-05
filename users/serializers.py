from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        mdoel = User
        fields = '__all__'

class UserSerializerToken(serializers.ModelSerializer):
    token = serializers.Field(source='my_token')

    class Meta:
        model = User
        fields = ('id', 'username', 'token')

class UserProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username')

