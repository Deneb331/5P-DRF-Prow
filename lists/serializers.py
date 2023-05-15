from rest_framework import serializers
from .models import List


class ListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = List
        fields = [
            'id', 'title', 'owner', 'created_at', 'board', 'is_owner'
        ]
