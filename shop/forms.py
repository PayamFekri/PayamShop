from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label= "",
        required=True,
        max_length= 50 , 
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your first name please*'})
    )
    
    last_name = forms.CharField(
        label= "",
        max_length= 50 , 
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your last name please'})
    )
    
    email = forms.EmailField(
        label= "",
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your Email address'})
    )
    
    username = forms.CharField(
        label= "",
        max_length= 20 , 
        required=True,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'get username please*'})
    )    
    password1 = forms.CharField(
        label="",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'name' : 'password',
                'type' : 'password', 
                'placeholder' : 'Enter more than 8 characters*'
                
            }
        )
    )
    
    
    password2 = forms.CharField(
        label="",
        required=True,
        widget= forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'name' : 'password',
                'type' : 'password', 
                'placeholder' : 'Enter your password again*'
                
            }
        )
    )
    
    class Meta:
        model = User
        fields = ("first_name" , 'last_name' ,"email","username","password1" ,"password2" )
        
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username