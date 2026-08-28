# Django CRM System

A Django-based Customer Relationship Management (CRM) application for managing customer records through a simple authenticated web interface.

The project demonstrates backend development with Django along with containerization and a basic CI pipeline using Jenkins.

## Features

- User registration and login
- Session-based authentication
- Protected CRM routes
- Add customer records
- View customer records
- Update customer records
- Delete customer records
- Form validation
- Bootstrap-based responsive UI
- SQLite database
- Dockerized application
- Persistent SQLite data using Docker volumes
- Jenkins CI pipeline
- GitHub webhook integration

## Tech Stack

- Python
- Django
- SQLite
- HTML/CSS
- Bootstrap
- Docker
- Jenkins
- Git/GitHub
- ngrok

## Project Structure

```
django-crm/
│
├── CRMProject/
│   ├── CRMApp/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── CRMProject/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── data/
│   │   └── db.sqlite3
│   │
│   └── manage.py
│
├── .gitignore
├── .dockerignore
├── .env
├── Dockerfile
├── Jenkinsfile
├── README.md
└── requirements.txt
```

## Local Setup

### Clone the Repository

```bash
git clone https://github.com/swaroopCh72/django-crm.git
cd django-crm
```

### Create Virtual Environment

```bash
python3 -m venv crmenv
```

### Activate Virtual Environment

#### Linux/macOS

```bash
source crmenv/bin/activate
```

#### Windows

```bash
crmenv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```
DJANGO_SECRET_KEY=your-secret-key
```

The secret key is intentionally kept outside version control.

### Run Migrations

```bash
cd CRMProject
python manage.py migrate
```

### Start Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

## Docker

Build the Docker image:

```bash
docker build -t django-crm:latest .
```

Run the application:

```bash
docker run --rm \
  --env-file .env \
  -p 8000:8000 \
  django-crm:latest
```

## Persistent Database with Docker Volume

The SQLite database is stored separately from the Docker image using a named volume.

Create the volume:

```bash
docker volume create django_crm_data
```

Run the application with the persistent volume:

```bash
docker run --rm \
  --env-file .env \
  -p 8000:8000 \
  -v django_crm_data:/app/CRMProject/data \
  django-crm:latest
```

The database persists even when the container is removed and recreated.

## CI Pipeline

Jenkins is configured to automatically build the project when changes are pushed to GitHub.

The pipeline performs:

1. Checkout source code
2. Create an isolated Python virtual environment
3. Install project dependencies
4. Run Django system checks
5. Run Django tests
6. Build the Docker image

### CI Workflow

```
Git Push
   │
   ▼
GitHub
   │
   │ Webhook
   ▼
ngrok
   │
   ▼
Jenkins
   │
   ├── Install Dependencies
   ├── Django Checks
   ├── Run Tests
   └── Docker Build
           │
           ▼
     django-crm:latest
```

## License

This project is for learning and portfolio purposes.
