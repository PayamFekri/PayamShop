from django.urls import path,include
from .views import helloworld , about , login_user , logout_user
urlpatterns = [
    path('hi/', helloworld, name='helloworld'),
    path('about/' , about),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout')
]
