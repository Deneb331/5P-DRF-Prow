from rest_framework import generics
from .models import Like
from .serializers import LikeSerializer
from drow_drfapi.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    """
    List all likes.
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Detail view of a single like, edit form and delete option.
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Like.objects.all()
