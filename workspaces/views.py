from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Workspace
from .serializers import WorkspaceSerializer


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
