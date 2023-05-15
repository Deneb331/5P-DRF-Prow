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


class ListDetail(APIView):
    """
    Detail view of a single list, edit form and delete option.
    """
    serializer_class = ListSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            listObj = List.objects.get(pk=pk)
            self.check_object_permissions(self.request, listObj)
            return listObj
        except List.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        listObj = self.get_object(pk)
        serializer = ListSerializer(
            listObj,
            context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        listObj = self.get_object(pk)
        serializer = ListSerializer(
            listObj,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        listObj = self.get_object(pk)
        listObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)