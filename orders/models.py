from django.db import models
from django.config import settings

# Create your models here.

class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places= 2, default = 0.00)
    status = models.CharField(max_length=20, default='pending')
    created_at  = models.DateTimeField(auto_now_add = True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)
    menu_item = models.ForeignKey('products.MenuItem', on_delete = models.PROTECT)
    quantity = models.PositiveIntegerField(default = 1)
    price = models.DecimalField(max_digits=10, decimal_places = 2 , default = 0.00 )

    def save(self,*args, **kwargs):
        if not self.price:
            try:
                self.price = self.menu_item.price
            except:
                self.price = 0.00
        super().save(*args,**kwargs)