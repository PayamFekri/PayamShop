from django.urls import path,include
from .views import helloworld , about
urlpatterns = [
    path('hi/', helloworld, name='helloworld'),
    path('about/' , about)
]
