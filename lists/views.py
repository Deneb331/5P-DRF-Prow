from rest_framework import generics
from drow_drfapi.permissions import IsOwnerOrReadOnly
from .models import List
from .serializers import ListSerializer


class ListList(generics.ListCreateAPIView):
    """
    List all lists.
    """
    serializer_class = ListSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = List.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view of a single list, edit form and delete option.
    """
    serializer_class = ListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = List.objects.all()
