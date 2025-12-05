from django.shortcuts import render , redirect , get_object_or_404
from .models import Product , Category ,Profile
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from . forms import SignUpForm , UpdateUserForm ,UpdatePasswordForm , UpdateUserInfo
from django.views.decorators.csrf import csrf_protect 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q

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

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, 'Your profile has been updated.')
            return redirect('helloworld')

        return render(request, 'shop/update_user.html', {'user_form': user_form})
    else:
        messages.error(request, 'First of all you have to Login!')
        return redirect('login')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = UpdatePasswordForm(current_user , request.POST)
            if form.is_valid():
                form.save()
                messages.success(request , 'edited password successfuly.')
                login(request , current_user)
                return redirect ('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.success(request , error)
                    return redirect('update_password')
        else:
            form = UpdatePasswordForm(current_user)
            return render(request , 'shop/update_password.html' , {'form':form})
    else:
        messages.success(request , 'first of all, you have to login')
        return redirect('helloworld')
    return render(request , 'shop/update_password.html' , {})

def update_info(request):
    if request.user.is_authenticated:
        current_user, created = Profile.objects.get_or_create(user=request.user)
        form = UpdateUserInfo(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile info has been updated.')
            return redirect('helloworld')

        return render(request, 'shop/update_info.html', {'form': form})
    else:
        messages.error(request, 'You must login first!')
        return redirect('login')

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
                return redirect("update_info")
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

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched = Product.objects.filter(Q(name__icontains = searched)| Q(description__icontains = searched))
        if not searched:
            messages.success(request , 'There is no such product')
            return render(request , 'shop/search.html' , {})
        else:
            return render(request , 'shop/search.html' , {'searched' : searched})
    return render(request , 'shop/search.html' , {})