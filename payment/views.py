from django.shortcuts import render ,redirect
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress  , Order
from django.contrib import messages

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

def confirm(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()
        user_shipping = request.POST
        request.session['user_shipping'] = user_shipping
        
        return render(request, 'payment/confirm.html', {
        'cart_products': cart_products,
        'quantities': quantities,
        'total': total,
        'shipping_info': user_shipping,})

    else:
        messages.success(request,'This page cannot be accessed')
        return redirect('helloworld')
    
    
    
def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods()
        quantities = cart.get_quants()
        total = cart.get_total()
        user_shipping = request.session.get('user_shipping')
        full_name = user_shipping['shipping_full_name']
        email = user_shipping['shipping_email']
        full_address = f'{user_shipping['shipping_address1']}\n{user_shipping['shipping_address2']}\n{user_shipping['shipping_city']}\n{user_shipping['shipping_state']}\n{user_shipping['shipping_zipcode']}\n{user_shipping['shipping_country']}\n'
        
        if request.user.is_authenticated:
            user = request.user
            new_order = Order(
                user = user,
                full_name = full_name,
                email = email , 
                shipping_address = full_address,
                amount_paid = total
            )
            new_order.save()
            messages.success(request,'The order was placed')
            return redirect('helloworld')
        else:
            new_order = Order(
                full_name = full_name,
                email = email , 
                shipping_address = full_address,
                amount_paid = total
            )
            new_order.save()
            messages.success(request,'The order was placed')
            return redirect('helloworld')
    else:
        messages.success(request,'This page cannot be accessed')
        return redirect('helloworld')