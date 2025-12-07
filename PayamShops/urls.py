from django.contrib import admin
from django.urls import path,include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('shop.urls')),
    path('cart/' , include('cart.urls')),
    path('payment/' , include('payment.urls'))
    ]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)

#django-admin startproject PayamShops

#python manage.py startapp shop

# python manage.py runserver

# http://127.0.0.1:8000/hi/

# python manage.py migrate -> create admin pannel

# python manage.py createsuperuser -> create admin user

# http://127.0.0.1:8000/admin/