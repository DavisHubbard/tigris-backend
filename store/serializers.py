from store.models import Item
from rest_framework import serializers
from django.contrib.auth.models import User


class ItemSerializer(serializers.HyperlinkedModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')

  class Meta:
      model = Item
      fields = ['url', 'created', 'title', 'description', 'price', 'item_type', 'owner']

class UserSerializer(serializers.HyperlinkedModelSerializer):
  items = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', read_only=True)

  class Meta:
    model = User
    fields = ['url', 'id', 'username', 'items']