from rest_framework import serializers

from .models import *


class PostSerializer(serializers.Serializer):
    subtitle = serializers.CharField(required=True)
    text = serializers.CharField(required=True)
    file = serializers.FileField(required=False)
    tag = serializers.CharField(required=False)
    release_date = serializers.CharField(required=False, source='get_release_date')
    release_time = serializers.CharField(required=False, source='get_release_time')
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        return Post.objects.create(**validated_data, user_id=user.id)