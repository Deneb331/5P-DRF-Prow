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


class CardDetail(APIView):
    """
    List a single card in detail and allows the user to edit or delete it.
    """
    serializer_class = CardSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            card = Card.objects.get(pk=pk)
            self.check_object_permissions(self.request, card)
            return card
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(
            card,
            context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(
            card,
            data=request.data,
            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
