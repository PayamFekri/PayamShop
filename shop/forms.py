from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm ,SetPasswordForm
from django import forms
from django.core.exceptions import ValidationError


class UpdateUserForm(UserChangeForm):
    password = None
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
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This email is already registered.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError("This username is already taken.")
        return username

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
    
    

class UpdatePasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
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
    
    
    new_password2 = forms.CharField(
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
        field = ['new_password1' ,'new_password2']