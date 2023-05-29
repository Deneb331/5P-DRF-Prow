from rest_framework import serializers
from .models import List
from cards.models import Card


class ListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    card_list = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_card_list(self, obj):
        card_list = Card.objects.filter(list=obj)
        serialized_card_list = [card.title for card in card_list]
        return serialized_card_list

    class Meta:
        model = List
        fields = [
            'id', 'title', 'owner', 'created_at', 'board', 'is_owner',
            'card_list'
        ]
