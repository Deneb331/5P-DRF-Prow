from rest_framework import generics
from drow_drfapi.permissions import IsOwnerOrReadOnly
from .models import Board
from .serializers import BoardSerializer


class BoardList(generics.ListCreateAPIView):
    """
    List all boards.
    """
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Board.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List a single board in detail and allows the user to edit or delete it.
    """
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Board.objects.all()
