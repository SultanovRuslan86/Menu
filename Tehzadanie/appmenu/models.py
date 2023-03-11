from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
    STATUS = (
        ('TRUE', 'True'),
        ('FALSE', 'False'),
    )
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']


class Product(models.Model):
    STATUS = (
        ('TRUE', 'True'),
        ('FALSE', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)



















