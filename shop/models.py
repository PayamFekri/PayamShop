from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator , MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length= 20)
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    phone = models.CharField(max_length= 20)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

SIZES = (
    ('m', 'Medium'),
    ('l', 'Large'),
    ('xl', 'Extra Large'),
    ('--', 'No Size'),
)

class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500 , default='' , blank=True , null=True)
    price = models.DecimalField(default=0 , decimal_places=2 , max_digits=15)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , default = 1)
    picture = models.ImageField(upload_to='upload/product')
    star = models.IntegerField(default = 0 , validators= [MaxValueValidator(5) ,MinValueValidator(0)])
    sale_price = models.DecimalField(default=0 , decimal_places=2 , max_digits=15)
    is_sale = models.BooleanField(default = False)
    size = models.CharField(max_length=10 , choices= SIZES , default= '--')
    is_available = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default='' , blank= True)
    phone = models.CharField(max_length=20 , blank= True)
    date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product

#هر موقع بخوای مدل هارو به دیتا بیس اضافه کنی
# یا تغییراتی در اونا به وجود بیاری
# باید دستورات زیر رو اجرا کنی
#command to add database: 
    # python manage.py makemigrations ->
        # python manage.py migrate -> 
            # added models to database