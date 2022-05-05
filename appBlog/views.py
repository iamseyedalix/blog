import json

from rest_framework import viewsets
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer
from users.serializers import UserSerializerToken, UserSerializer

class PostView(viewsets.ViewSet):
    def list(self, request):
        queryset = Post.objects.all().order_by('-release_date')[:5]
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, permission_classes=([IsAuthenticated]))
    def create(self, request):
        print(request.data)
        serializer = PostSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
