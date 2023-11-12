from django.db import models
from django.db.models import PROTECT

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category name')
    description = models.TextField(**NULLABLE, verbose_name='Description')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('pk',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product name')
    description = models.TextField(**NULLABLE, verbose_name='Description')
    photo = models.ImageField(upload_to='db_store/', **NULLABLE, verbose_name='Picture')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category name')
    price = models.FloatField(**NULLABLE, verbose_name='Product price')
    creation_date = models.DateField(auto_now=False, auto_now_add=True, verbose_name='Creation date')
    changing_date = models.DateField(auto_now=True, auto_now_add=False, verbose_name='Last changed date')

    def __str__(self):
        return f'{self.name} ({self.category}) тг.'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
