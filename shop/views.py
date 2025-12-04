from django.shortcuts import render , redirect , get_object_or_404
from .models import Product , Category
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from . forms import SignUpForm
from django.views.decorators.csrf import csrf_protect  # اضافه کنید

@csrf_protect
def helloworld(request):
    all_product = Product.objects.all()
    return render(request, 'shop/index.html', {'ProductsINview' : all_product})

def about(request):
    return render(request , 'shop/about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username , password = password)
        if user is not None : 
            login(request , user)
            messages.success(request , "Logged in successfully.")
            return redirect("helloworld")
        else:
            messages.success(request , "Logged in UNsuccessfully!")
            return redirect("login")
    else :
        return render(request , 'shop/login.html')

def logout_user(request):
    logout(request)
    messages.success(request , ("You have successfully logged out."))
    return redirect("helloworld")

def signup_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, "Sign up is successfully.")
                return redirect("helloworld")
            else:
                messages.error(request, "Authentication failed after signup.")
                return redirect("signup")
        else:
            # نمایش خطاهای فرم
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            return render(request, 'shop/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'shop/signup.html', {'form': form})

def product(request , pk):
    product = Product.objects.get(id = pk)
    return render(request , 'shop/product.html' , {'product' : product})


def category(request , cat):
    cat = cat.replace('-', ' ')
    try:
        category = Category.objects.get(name = cat)
        products= Product.objects.filter(category = category)
        return render(request , 'shop/category.html' , {'ProductsINview' : products , "category" : category})
    except:
        messages.success(request , ("category isn't exist"))
        return redirect("helloworld")
def category_summary(request):
    all_cat = Category.objects.all()
    return render(request , 'shop/category_summary.html' , {'category':all_cat})