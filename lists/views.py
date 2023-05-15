from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import List
from .serializers import ListSerializer
from drow_drfapi.permissions import IsOwnerOrReadOnly


class ListList(APIView):
    """
    List all lists.
    """
    serializer_class = ListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        lists = List.objects.all()
        serializer = ListSerializer(
            lists,
            many=True,
            context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = ListSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)