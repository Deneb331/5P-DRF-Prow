from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drow_drfapi.permissions import IsOwnerOrReadOnly
from .models import Card
from .serializers import CardSerializer


class CardList(APIView):
    """
    List all cards.
    """
    serializer_class = CardSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        cards = Card.objects.all()
        serializer = CardSerializer(
            cards,
            many=True,
            context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CardSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)