from django.db.models import Count
from rest_framework import generics, filters
from drow_drfapi.permissions import IsOwnerOrReadOnly
from .models import Board
from .serializers import BoardSerializer


class BoardList(generics.ListCreateAPIView):
    """
    List all boards.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Board.objects.annotate(
        lists_count=Count('owner__list', distinct=True),
        cards_count=Count('owner__card', distinct=True),
        members_count=Count('owner__profile', distinct=True)
    ).order_by('-created_on')

    serializer_class = BoardSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title'
    ]
    ordering_fields = [
        'lists_count',
        'cards_count',
        'members_count'
    ]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List a single board in detail and allows the user to edit or delete it.
    """
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Board.objects.annotate(
        lists_count=Count('owner__list', distinct=True),
        cards_count=Count('owner__card', distinct=True),
        members_count=Count('owner__profile', distinct=True)
    ).order_by('-created_on')
