from rest_framework import serializers
from .models import Tree


class ThreeCreateSerializer(serializers.ModelSerializer):
    """Добавление элемента дерева"""

    class Meta:
        model = Tree
        fields = '__all__'


class FilterThreeSerializer(serializers.ListSerializer):
    """Фильтр элементов дерева, только корневые элементы"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = TreeSeializer(value, context=self.context)
        return serializer.data


class TreeSeializer(serializers.ModelSerializer):
    """Вывод дерева"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterThreeSerializer
        model = Tree
        fields = ('id', 'name', 'children')
