from django.db import models

# django-filer
from filer.fields.image import FilerImageField
from django.contrib.auth.models import User


# 自訂User，但其實可以直接用auth提供的即可
# class User(models.Model):
#     username = models.CharField(max_length=20, null=False)
#     email = models.EmailField()
#     password = models.CharField(max_length=20, null=False)
#     enabled = models.BooleanField(default=False)  # 是否為會員

#     def __str__(self):
#         return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 一個user對應到一個profile
    male = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # 外來鍵連到Category的主鍵
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.TextField()
    # image = models.URLField(null=True)
    image = FilerImageField(related_name='product_image', on_delete=models.CASCADE)  # 外部連結顯示圖片
    website = models.URLField(null=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add: 建立時的時間，往後修改model不會更新
    updated_at = models.DateTimeField(auto_now=True)  # auto_now: 每次save都更新為當前的時間
    # datetimefield: 日期+時間, datefield: 日期
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'Order:{self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    # Heroku無法修改cart.py的model，所以暫時不join到product
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default=None)
    
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

