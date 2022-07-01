from rest_framework import viewsets, mixins
from .serializers import TreeSeializer, ThreeCreateSerializer

from .models import Tree


class MyViewSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    pass


class TreeViewSet(MyViewSet):
    """Вывод списка дерева, создание, удаление, вывод ветки """
    # serializer_class = TreeSeializer
    queryset = Tree.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ThreeCreateSerializer
        else:
            return TreeSeializer
