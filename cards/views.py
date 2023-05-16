from rest_framework import generics, permissions
from .models import Card
from .serializers import CardSerializer


class CardList(generics.ListCreateAPIView):
    """
    List all cards.
    """
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Card.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List a single card in detail and allows the user to edit or delete it.
    """
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]

    queryset = Card.objects.all()
