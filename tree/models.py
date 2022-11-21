from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Tree(MPTTModel):
    "Модель дерева"
    parent = TreeForeignKey('self', models.CASCADE, null=True, blank=True, verbose_name='Родитель',
                            related_name='children')
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return f'{self.pk}-{self.name}'
