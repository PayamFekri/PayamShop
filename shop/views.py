from django.shortcuts import render , HttpResponse

def helloworld(request):
    return render(request, 'shop/index.html')


