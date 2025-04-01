# 🍽️ DineX - Restaurant Management System

![DineX Banner](https://via.placeholder.com/1200x400?text=DineX+Restaurant+Management+System)

Welcome to **DineX**, a modern and efficient **Restaurant Management System** designed to streamline restaurant operations. Built with **Django** and **Tailwind CSS**, it provides a user-friendly interface for managing categories, products, and orders.

---

## 🌟 Features

### 🏢 Admin Panel
✅ **Manage Categories & Subcategories** (Add/Edit/Delete)  
✅ **Manage Products** (Add/Edit/Delete)  
✅ **Order Management**  
✅ **Secure Authentication**

### 🍽️ Menu & Ordering System
✔️ Browse diverse **food categories**  
✔️ View **detailed product descriptions**  
✔️ **Search & Filter** for easy navigation

### 🛒 Cart & Checkout
🛍️ Add items to the **cart**  
💰 Dynamic **total price calculation**  
🔒 Secure & smooth **checkout process**

### 🔐 Authentication & Security
🔑 **User Login & Logout System**  
🛡️ **Custom Middleware** for session security  
📌 **Admin Panel Protection**

---

## 🏗️ Tech Stack

| Backend | Frontend | Database | Authentication |
|---------|---------|----------|---------------|
| Django (Python) | Tailwind CSS, HTML, JavaScript | SQLite / PostgreSQL | Django Auth, Custom Middleware |

---

## 🚀 Installation Guide

### 📥 1️⃣ Clone the Repository
```bash
   git clone https://github.com/aloksingh72/DineX.git
   cd DineX
```

### 🏗️ 2️⃣ Create a Virtual Environment
```bash
   python -m venv env
   source env/bin/activate  # (Linux/Mac)
   env\Scripts\activate  # (Windows)
```

### 📦 3️⃣ Install Dependencies
```bash
   pip install -r requirements.txt
```

### 🔄 4️⃣ Run Migrations
```bash
   python manage.py makemigrations
   python manage.py migrate
```

### 🔑 5️⃣ Create Superuser
```bash
   python manage.py createsuperuser
```

### ▶️ 6️⃣ Run the Server
```bash
   python manage.py runserver
```

🎯 Open **`http://127.0.0.1:8000/`** in your browser 🚀

---

## 🛡️ Custom Middleware for Secure Logout
To prevent users from accessing **admin pages after logout**, we use a **custom Django middleware**:

```python
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout

class LogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith("/static/") or request.path.startswith("/media/"):
            return None  
        if request.path == "/admin-login/":
            return None  
        if not request.user.is_authenticated:
            return redirect("/admin-login/")
        return None
```

---



---

## 🤝 Contribution
🛠️ Contributions are **welcome!** If you'd like to improve **DineX**, feel free to **fork the repo** and submit a **pull request**.

---

## 📧 Contact
📩 Reach out to me at **[aloksingh36757@gmail.com](mailto:aloksingh36757@gmail.com)**.

---

✨ **DineX - Bringing Restaurants Online!** 🍕🍜
