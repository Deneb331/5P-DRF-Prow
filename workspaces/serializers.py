from rest_framework import serializers
from profiles.models import Profile
from boards.models import Board
from .models import Workspace


class WorkspaceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    member_list = serializers.SerializerMethodField()
    board_list = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_member_list(self, obj):
        member_list = Profile.objects.filter(workspaces=obj)
        serialized_member_list = [
            profile.name for profile in member_list
        ]
        return serialized_member_list

    def get_board_list(self, obj):
        board_list = Board.objects.filter(workspace=obj)
        serialized_board_list = [board.title for board in board_list]
        return serialized_board_list

    class Meta:
        model = Workspace
        fields = [
            'id', 'title', 'owner', 'updated_at', 'is_owner',
            'member_list', 'board_list'
        ]
