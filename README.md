🍽️ DineX - Restaurant Management System

DineX is a modern restaurant management system designed to streamline restaurant operations. It includes features like category and product management, an intuitive admin panel, and a well-structured UI built with Django and Tailwind CSS.

🚀 Features

🌟 Admin Panel

Add/Edit/Delete Categories and Subcategories

Add/Edit/Delete Products

Manage orders efficiently

Secure admin authentication

🍔 Menu Management

Browse various food categories

View detailed product descriptions

Easy search and filtering options

🛒 Cart & Ordering

Add items to the cart

Calculate total price dynamically

Seamless checkout process

🔒 Authentication & Security

Login & Logout System

Custom middleware to prevent unauthorized access

Secure session handling

🏗️ Tech Stack

Backend: Django (Python)

Frontend: Tailwind CSS, HTML, JavaScript

Database: SQLite / PostgreSQL

Authentication: Django Auth, Custom Middleware

🛠️ Installation Guide

1️⃣ Clone the Repository

   git clone https://github.com/aloksingh72/DineX.git
   cd DineX

2️⃣ Create a Virtual Environment

   python -m venv env
   source env/bin/activate  # (Linux/Mac)
   env\Scripts\activate  # (Windows)

3️⃣ Install Dependencies

   pip install -r requirements.txt

4️⃣ Run Migrations

   python manage.py makemigrations
   python manage.py migrate

5️⃣ Create Superuser

   python manage.py createsuperuser

6️⃣ Run the Server

   python manage.py runserver

Now, open your browser and go to http://127.0.0.1:8000/ 🚀

🛡️ Middleware for Logout Security

To prevent users from accessing admin pages after logout, we use custom middleware:

🤝 Contribution

Contributions are welcome! Feel free to fork and submit PRs.

📧 Contact

For any queries, reach out to me at aloksingh36757@gmail.com.

✨ DineX - Bringing Restaurants Online! 🍕🍜

