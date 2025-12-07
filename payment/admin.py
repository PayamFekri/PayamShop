from django.contrib import admin
from .models import ShippingAddress



# Register your models here.
#-------------------------
#how to install payment app 
#in cmd at your directory:
# -> python manage.py startapp payment
#-------------------------

admin.site.register(ShippingAddress)