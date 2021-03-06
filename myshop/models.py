from django.db import models

# django-filer
from filer.fields.image import FilerImageField


# 自訂User，但其實可以直接用auth提供的即可
class User(models.Model):
    username = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)  # 是否為會員

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # 外來鍵連到Category的主鍵
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = FilerImageField(related_name='product_image', on_delete=models.CASCADE)  # 外部連結顯示圖片
    website = models.URLField(null=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name