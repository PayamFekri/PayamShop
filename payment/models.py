from django.db import models
from django.contrib.auth.models import User
from shop.models import Product

class ShippingAddress(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank= True )
    shipping_full_name  = models.CharField(max_length=250)
    shipping_email = models.CharField(max_length= 300) 
    shipping_phone = models.CharField(max_length=40,blank= True)
    shipping_address1 = models.CharField(max_length=300,blank= True)
    shipping_address2 = models.CharField(max_length=300,null=True,blank= True)
    shipping_city = models.CharField(max_length=40,blank= True)
    shipping_state = models.CharField(max_length=40,blank= True)
    shipping_zipcode = models.CharField(max_length=40,blank= True)
    shipping_country = models.CharField(max_length=40,default= 'Iran')
    
    def __str__(self):
        return f'Shipping Address From {self.shipping_full_name}'
    
class Order(models.Model):
    STATUS_ORDER = [
        ('Pending' , 'waiting payment'),
        ('Processing' , 'Processing'),
        ('Shipped' , 'Sent to the post'),
        ('Delivered' , 'Delivered'),
    ]
    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True , blank= True )
    full_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=300)
    shipping_address = models.TextField(max_length=150000)
    amount_paid = models.DecimalField(decimal_places=2 , max_digits=15)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=50 , choices=STATUS_ORDER , default='Pending')
    
    def __str__(self):
        return f'Order - {str(self.id)}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , null= True)
    product = models.ForeignKey(Product , on_delete=models.CASCADE , null= True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , null= True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(decimal_places=2 , max_digits=15)
    def __str__(self):
        if self.user is not None:
            return f'Order Item {str(self.id)} - for {self.user}'
        else:
            return f'Order Item {str(self.id)}'