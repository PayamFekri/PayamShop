from django.shortcuts import render , redirect , get_object_or_404
from .models import Product , Category ,Profile
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from . forms import SignUpForm , UpdateUserForm ,UpdatePasswordForm , UpdateUserInfo
from django.views.decorators.csrf import csrf_protect 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
import json , ast
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress ,Order ,OrderItem
def order_details(request,pk):
    if request.user.is_authenticated:
        order = Order.objects.get(id = pk)
        items = OrderItem.objects.filter(order = pk)
        context = {
            'order' : order,
            'items' : items
        }
        
        return render(request, 'shop/order_details.html' , context)
    else:
        messages.success(request , 'دسترسی به این صفحه امکان پذیر نمیباشد')
        return redirect("helloworld")
    

def user_orders(request):
    if request.user.is_authenticated:
        delivered_orders = Order.objects.filter(user = request.user , status= 'Delivered')
        other_orders = Order.objects.filter(user = request.user).exclude(status= 'Delivered')
        
        context = {
            'delivered' : delivered_orders,
            'other' : other_orders
        }
        
        return render(request, 'shop/orders.html', context)
    else:
        messages.success(request , 'دسترسی به این صفحه امکان پذیر نمیباشد')
        return redirect("helloworld")


@csrf_protect
def helloworld(request):
    all_product = Product.objects.all()
    return render(request, 'shop/index.html', {'ProductsINview' : all_product})

def about(request):
    return render(request , 'shop/about.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # گرفتن پروفایل کاربر
            try:
                current_user = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                current_user = None

            # اگر پروفایل و سبد قدیمی وجود داشت
            if current_user and current_user.old_cart:
                saved_cart = current_user.old_cart
                try:
                    # تلاش برای خواندن JSON معتبر
                    converted_cart = json.loads(saved_cart)
                except json.JSONDecodeError:
                    # اگر داده قدیمی بود (str(dict))، با ast تبدیل کن
                    converted_cart = ast.literal_eval(saved_cart)
                    # و دوباره درست ذخیره کن
                    current_user.old_cart = json.dumps(converted_cart)
                    current_user.save()

                # اضافه کردن محصولات به سبد session
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

            messages.success(request, "Logged in successfully.")
            return redirect("helloworld")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    # اگر متد POST نبود
    return render(request, 'shop/login.html')


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
        shipping_user, created = ShippingAddress.objects.get_or_create(user=request.user)

        form = UpdateUserInfo(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, 'Your profile info has been updated.')
            return redirect('helloworld')

        return render(request, 'shop/update_info.html', {
            'form': form,
            'shipping_form': shipping_form
        })
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