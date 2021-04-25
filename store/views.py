from store.models import Item
from store.serializers import ItemSerializer, UserSerializer
from store.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

@api_view(['GET'])
def api_root(request, format=None):
  return Response({'users': reverse('user-list', request=request, format=format),
        'items': reverse('item-list', request=request, format=format)})

class ItemViewSet(viewsets.ModelViewSet):
  """
  This viewset automatically provides `list`, `create`, `retrieve`,
  `update` and `destroy` actions.
  """
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
  """
  This viewset automatically provides `list` and `retrieve` actions.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer