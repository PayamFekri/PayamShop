from django.shortcuts import render , get_object_or_404
from .cart import Cart
from shop.models import Product
from django.http import JsonResponse



def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    return render(request , 'cart_summary.html' , {'cart_products':cart_products , 'quantities' :quantities})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product_qty = request.POST.get('product_qty')
        if not product_id:
            return JsonResponse({'error': 'No product id provided'}, status=400)
        product = get_object_or_404(Product, id=int(product_id))
        cart.add(product=product , quantity = product_qty)
        cart_quantity  = cart.__len__()
        
        return JsonResponse({'product_name': product.name , 'qty': cart_quantity})

def cart_delete(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))

        if not product_id:
            return JsonResponse({'error': 'No product id provided'}, status=400)
        cart.delete(product = product_id)
        return JsonResponse({'product': product_id})


def cart_update(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        if not product_id:
            return JsonResponse({'error': 'No product id provided'}, status=400)
        product = get_object_or_404(Product, id=int(product_id))
        cart.update(product=product , quantity = product_qty)        
        return JsonResponse({'product_name': product.name , 'qty': product_qty})

