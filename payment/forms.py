from django import forms
from .models import ShippingAddress

class ShippingForm (forms.ModelForm):
    shipping_full_name = forms.CharField(
        label= "",
        required=True,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Full Name'})
    )
    shipping_email = forms.CharField(
        label= "",
        required=True,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'E-mailshipping_'})
    )    
    shipping_address1 = forms.CharField(
        label= "",
        required=True,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'first addres'})
    )
    shipping_address2 = forms.CharField(
        label= "",
        required=False,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'second address'})
    )
    shipping_city = forms.CharField(
        label= "",
        required=True,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'city'})
    )
    shipping_state = forms.CharField(
        label= "",
        required=False,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'state'})
    )
    shipping_zipcode = forms.CharField(
        label= "",
        required=False,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'zip-code'})
    )
    shipping_country = forms.CharField(
        label= "",
        required=True,
        widget= forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'country'})
    )
    
    
    class Meta:
        model = ShippingAddress
        fields =[
                'shipping_full_name', 
                'shipping_email', 
                'shipping_phone',
                'shipping_address1',    
                'shipping_address2',    
                'shipping_city',    
                'shipping_state',    
                'shipping_zipcode',    
                'shipping_country'
        ]
        
        exclude =['user',]
