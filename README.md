# Client Task Tracker

A Django + Django REST Framework backend project for managing clients and tasks.

## Features

- User authentication with Django admin
- Client management
- Task management
- Token support
- Admin dashboard for managing project data

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite

## Setup

```bash
git clone https://github.com/40jon/client-task-tracker.git
cd client-task-tracker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
