from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField('Category', max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField('Product', max_length=150)
    photo = models.ImageField('Photo of product', upload_to='products/')
    description = models.TextField('Description')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


