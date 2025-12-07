# PayamShop 🛒

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)

PayamShop یک فروشگاه آنلاین ساده با Django است که روند کامل خرید آنلاین را نمایش می‌دهد — از لیست محصولات تا سبد خرید، تسویه و پرداخت.  

This is a simple online shop built with Django, demonstrating a full shopping flow — from product listing to cart, checkout, and payment.

🌐 Demo: [Live Demo Link](https://payamfekri.pythonanywhere.com/hi/)  

---

## ✅ ویژگی‌ها / Features

- 📦 نمایش محصولات با دسته‌بندی و تصاویر / Product listing with categories & images  
- 🔍 صفحه جزئیات محصول / Product detail page  
- 🛒 سبد خرید: افزودن، حذف و بروزرسانی آیتم‌ها / Shopping cart: add/remove/update items  
- 💳 فرایند تسویه و پرداخت ساده / Checkout & payment flow (basic)  
- 📸 پشتیبانی از آپلود تصاویر / Image upload support  
- 🌐 پشتیبانی از فایل‌های استاتیک / Static files (CSS/JS/images)  
- 🗄️ پایگاه داده SQLite پیش‌فرض / Default SQLite backend  

---

## 🛠 تکنولوژی‌ها / Tech Stack

- Backend: Python 3.x, Django 4.x  
- Frontend: HTML, CSS, JavaScript  
- Database: SQLite (development)  
- Deployment: WSGI-compatible server (optional)  

---

## 📦 نصب و راه‌اندازی / Installation

`bash
git clone https://github.com/PayamFekri/PayamShop.git
cd PayamShop

# (اختیاری) ایجاد virtual environment
python3 -m venv venv
source venv/bin/activate   # ویندوز: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser 
# اگر می‌خواید ادمین داشته باشید

python manage.py runserver