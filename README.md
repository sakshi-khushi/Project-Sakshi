# sakshi_LMS

A Django-based Learning Management System (LMS) that provides RESTful APIs for user registration, user management, and course uploads. The system supports two user types: Teacher and Student.

## Features

- User signup with user type (Teacher/Student)
- View all users
- Update user email
- Delete user by number
- Upload and manage courses (for teachers)
- SQLite database for development

## Project Structure


sakshi_LMS/
├── db.sqlite3
├── manage.py
├── sakshi_COURSES/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serlizers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
└── sakshi_LMS/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


## Setup Instructions

1. *Clone the repository:*
   sh
   git clone hhttps://github.com/sakshi-khushi/Project-Sakshi.git
   cd sakshi_LMS
   

2. *Create a virtual environment and activate it:*
   sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   

3. *Install dependencies:*
   sh
   pip install -r requirements.txt
   

4. *Apply migrations:*
   sh
   python manage.py migrate
   

5. *Run the development server:*
   sh
   python manage.py runserver
   

6. *API Endpoints:*
   - POST /signup/ - Register a new user
   - GET /getAllUsers/ - List all users
   - PUT /updateEmail/ - Update user email
   - DELETE /deleteUser/<number>/ - Delete user by number
