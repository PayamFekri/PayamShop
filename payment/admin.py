from django.contrib import admin
from .models import ShippingAddress , Order , OrderItem



# Register your models here.
#-------------------------
#how to install payment app 
#in cmd at your directory:
# -> python manage.py startapp payment
#-------------------------

admin.site.register(ShippingAddress)
#admin.site.register(Order)
admin.site.register(OrderItem)

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0 
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['date_ordered' , 'last_update']
    inlines = [OrderItemInLine]