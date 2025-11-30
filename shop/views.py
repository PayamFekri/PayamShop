from django.shortcuts import render , HttpResponse
from .models import Product
def helloworld(request):
    all_product = Product.objects.all()
    return render(request, 'shop/index.html', {'ProductsINview' : all_product})


