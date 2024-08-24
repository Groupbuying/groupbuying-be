from django.db import models

from users.models import User, NonRegisteredUser


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)


class Category(models.Model):
    name = models.CharField(max_length=100)


class GroupCart(models.Model):
    name = models.CharField(max_length=100, default='')


class GroupCartItem(models.Model):
    cart = models.ForeignKey(GroupCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vote_up = models.IntegerField(default=0)
    vote_down = models.IntegerField(default=0)
    is_selected = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    non_registed_user = models.ForeignKey(NonRegisteredUser, on_delete=models.CASCADE, null=True)


class OrderStatus(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    cart = models.ForeignKey(GroupCart, on_delete=models.CASCADE)
    paid_at = models.DateTimeField(null=True)
