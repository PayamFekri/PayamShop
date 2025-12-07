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
## Project Structure

PayamShop/
    PayamShop/

    ├── shop/              Shop app: product listing, detail, cart, checkout

    ├── cart/             # Shopping cart functionality
    
    ├── payment/          # Payment processing module/app
    
    ├── media/            # Uploaded product images
    
    ├── static/           # CSS / JS / frontend assets
    
    ├── manage.py         # Django management script
    
    ├── requirements.txt  # Python dependencies
    
    └── db.sqlite3        # Default SQLite database (development)
---
## 📂 Project Structure 
Here is the overall structure of the **PayamShop** project with a brief explanation of each folder and file: 

PayamShop/ ├── shop/ # Main shop application │ ├── migrations/ # Django database migrations for the shop app │ ├── templates/ # HTML templates (product listing, detail pages, checkout, etc.) │ ├── static/ # Static files specific to the shop app (CSS/JS/images) │ ├── models.py # Defines product, category, and other database models │ ├── views.py # Views for displaying products and handling shop logic │ ├── urls.py # URL routes for the shop app │ └── admin.py # Django admin configurations for managing products

├── cart/ # Shopping cart application │ ├── models.py # Cart-related models (if needed) │ ├── views.py # Logic for adding/removing/updating items in the cart │ └── urls.py # URL routes for cart functionality

├── payment/ # Payment application │ ├── views.py # Handles payment processing logic │ └── urls.py # URL routes for payment endpoints

├── media/ # Uploaded product images (user-generated content) ├── static/ # Global static files (CSS, JS, images shared across the project) ├── manage.py # Django management script (runserver, migrations, etc.) ├── requirements.txt # Python dependencies required for the project └── db.sqlite3 # SQLite database (default, for development/testing)

### ✅ Notes: - The **shop/** app is the core of the project, handling product display, detail views, and checkout flowcart/*cart/** app handles the shopping cart logic separately for modularity. - The **payment/** app is responsible for processing payments, currently implemented as a simple placeholder for learning/demo media/- **media/** is where product images uploaded by users arstatic/ **static/** contains global frontend assets shared across thedb.sqlite3db.sqlite3** is for development only; in production, a more robust database should be used (e.g., PostgreSQL). --- This structure is modular, making it easy to extend each component independently — for example, adding user accounts, order history, or integrating real payment gateways in the future. 
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

# how to run

python manage.py runserver
