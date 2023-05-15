from rest_framework import serializers
from .models import Card


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Card
        fields = [
            'id', 'title', 'owner', 'list', 'content', 'member',
            'priority_color', 'created_on', 'updated_on',
            'due_time', 'is_owner', 'file'
        ]
