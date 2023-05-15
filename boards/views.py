from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drow_drfapi.permissions import IsOwnerOrReadOnly
from .models import Board
from .serializers import BoardSerializer


class BoardList(APIView):
    """
    List all boards.
    """
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(
            boards,
            many=True,
            context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = BoardSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetail(APIView):
    """
    List a single board in detail and allows the user to edit or delete it.
    """
    serializer_class = BoardSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            board = Board.objects.get(pk=pk)
            self.check_object_permissions(self.request, board)
            return board
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(
            board,
            context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        board = self.get_object(pk)
        serializer = BoardSerializer(
            board,
            data=request.data,
            context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        board = self.get_object(pk)
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
