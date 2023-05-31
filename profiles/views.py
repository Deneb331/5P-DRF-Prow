from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from drow_drfapi.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    """
    queryset = Profile.objects.annotate(
        boards_count=Count('owner__board', distinct=True),
        lists_count=Count('owner__list', distinct=True),
        cards_count=Count('owner__card', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'name'
    ]
    ordering_fields = [
        'boards_count',
        'lists_count',
        'cards_count'
    ]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List a single profile in detail and allows the user to edit or destroy it.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.annotate(
        boards_count = Count('owner__board', distinct=True),
        lists_count =  Count('owner__list', distinct=True),
        cards_count = Count('owner__card', distinct=True)
    ).order_by('-created_at')
