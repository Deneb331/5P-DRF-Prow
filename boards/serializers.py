from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    lists_count = serializers.ReadOnlyField()
    cards_count = serializers.ReadOnlyField()
    members_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Board
        fields = [
            'id', 'title', 'owner', 'workspace', 'created_on',
            'updated_on', 'is_owner', 'image', 'lists_count',
            'cards_count', 'members_count',
        ]
