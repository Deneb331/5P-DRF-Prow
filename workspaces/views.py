from rest_framework import generics
from drow_drfapi.permissions import IsOwnerOrReadOnly
from .models import Workspace
from .serializers import WorkspaceSerializer


class WorkspaceList(generics.ListCreateAPIView):
    """
    List all workspaces.
    """
    serializer_class = WorkspaceSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Workspace.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WorkspaceDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Detail view of a single workspace, edit form and delete option.
    """
    serializer_class = WorkspaceSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Workspace.objects.all()
