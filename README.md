# Django CRM System

A simple Customer Relationship Management (CRM) web application built using Django.

The application allows authenticated users to manage customer records with complete CRUD functionality.

## Features

- User Registration and Login
- Session-based Authentication
- Add Customer Records
- View Customer Details
- Update Existing Records
- Delete Records
- Form Validation
- Protected Routes for Authorized Users
- Bootstrap-based Responsive UI
- Dockerized Development Setup

---

## Tech Stack

- Python
- Django
- SQLite
- Bootstrap
- HTML/CSS
- Docker

---

## Project Structure

```bash
django-crm-system/
│
├── crm/
├── website/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── Dockerfile
└── db.sqlite3
```

---

## Installation

### Clone the Repository

```bash
git clone <https://github.com/your-username/django-crm-system.git>
cd django-crm-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\\Scripts\\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py migrate
```

---

## Start Development Server

```bash
python manage.py runserver
```

Open browser and visit:

```bash
<http://127.0.0.1:8000/>
```

Testing webhooks T1