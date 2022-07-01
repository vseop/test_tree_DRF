from django.shortcuts import render
from .models import Tree

from rest_framework import viewsets, mixins
from .serializers import *


class MyViewSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    pass


class TreeViewSet(MyViewSet):
    # serializer_class = TreeSeializer
    queryset = Tree.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ThreeCreateSerializer
        else:
            return TreeSeializer
