from rest_framework import serializers
from boards.models import Board
from .models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    board_list = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_board_list(self, obj):
        board_list = Board.objects.filter(workspace=obj)
        serialized_board_list = [board.title for board in board_list]
        return serialized_board_list

    class Meta:
        model = Workspace
        fields = [
            'id', 'title', 'owner', 'updated_at', 'is_owner',
            'board_list'
        ]
