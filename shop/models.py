from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator , MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now= True)
    phone = models.CharField(max_length=40,blank= True)
    address1 = models.CharField(max_length=300,blank= True)
    address2 = models.CharField(max_length=300,blank= True)
    city = models.CharField(max_length=40,blank= True)
    state = models.CharField(max_length=40,blank= True)
    zipcode = models.CharField(max_length=40,blank= True)
    country = models.CharField(max_length=40,default= 'Iran')
    old_cart = models.CharField(max_length=200 , blank=True ,null=True)
    
    def __str__(self):
        return self.user.username
    
def create_profile(sender , instance , created , **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
post_save.connect(create_profile , sender=User)

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
    address = models.CharField(max_length=20, default='' , blank= True)
    phone = models.CharField(max_length=500 , blank= True)
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