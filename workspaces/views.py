from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Workspace
from .serializers import WorkspaceSerializer
from drow_drfapi.permissions import IsOwnerOrReadOnly


class WorkspaceList(APIView):
    """
    List all workspaces.
    """
    serializer_class = WorkspaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        workspaces = Workspace.objects.all()
        serializer = WorkspaceSerializer(
            workspaces,
            many=True,
            context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkspaceSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkspaceDetail(APIView):
    """
    Detail view of a single workspace, edit form and delete option.
    """
    serializer_class = WorkspaceSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            workspace = Workspace.objects.get(pk=pk)
            self.check_object_permissions(self.request, workspace)
            return workspace
        except Workspace.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        workspace = self.get_object(pk)
        serializer = WorkspaceSerializer(
            workspace,
            context={'request': request}
        )
        return Response(serializer.data)
    
    def put(self, request, pk):
        workspace = self.get_object(pk)
        serializer = WorkspaceSerializer(
            workspace,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        workspace = self.get_object(pk)
        workspace.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)