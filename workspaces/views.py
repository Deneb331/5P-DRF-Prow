from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Workspace
from .serializers import WorkspaceSerializer


class WorkspaceList(APIView):
    """
    List all workspaces.
    """
    def get(self, request):
        workspaces = Workspace.objects.all()
        serializer = WorkspaceSerializer(
            workspaces, 
            many=True,
            context={'request': request})
        return Response(serializer.data)
