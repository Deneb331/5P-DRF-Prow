from rest_framework import serializers
from cards.models import Card
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    card_list = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_card_list(self, obj):
        user = self.context['request'].user
        card_list = Card.objects.filter(members=obj.owner)
        if user.is_authenticated:
            serialized_card_list = [card.title for card in card_list]
            return serialized_card_list
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'name', 'content', 'image', 'is_owner',
            'workspaces', 'card_list'
        ]
