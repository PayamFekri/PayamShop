from django.shortcuts import render , get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse



def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request , 'cart_summary.html' , {'cart_products':cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        if not product_id:
            return JsonResponse({'error': 'No product id provided'}, status=400)
        product = get_object_or_404(Product, id=int(product_id))
        cart.add(product=product)
        cart_quantity  = cart.__len__()
        
        return JsonResponse({'product_name': product.name , 'qty': cart_quantity})

def cart_delete(request):
    pass

def cart_update(request):
    pass
