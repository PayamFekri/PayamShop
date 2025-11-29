from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('shop.urls'))
]

# python manage.py runserver
# http://127.0.0.1:8000/hi/