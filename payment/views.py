from django.shortcuts import render
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress

def payment_success(request):
    return render(request , 'payment/payment_success.html' , {})

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    total = cart.get_total()

    if request.user.is_authenticated:
        # فقط شیء مدل رو بگیر، نه tuple
        shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
    else:
        shipping_form = ShippingForm(request.POST or None)

    return render(request, 'payment/checkout.html', {
        'cart_products': cart_products,
        'quantities': quantities,
        'total': total,
        'shipping_form': shipping_form,
    })
