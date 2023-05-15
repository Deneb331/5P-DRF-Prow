from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Like
from .serializers import LikeSerializer
from drow_drfapi.permissions import IsOwnerOrReadOnly


class LikeList(APIView):
    """
    List all likes.
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(
            likes,
            many=True,
            context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = LikeSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)