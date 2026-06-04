# Student Management System

A Django web application for managing students, courses, absences, and multi-channel notifications.

## Features

- **Student Management** — Full CRUD (create, read, update, delete) with paginated list and detail views
- **Course Management** — Create and track training programs
- **Absence Tracking** — Record absences with justifications
- **Multi-channel Notifications** — In-app, email (Gmail SMTP), and SMS (Twilio)
- **Automation** — Automatic notification (in-app + email) when an absence is recorded
- **Internationalization** — FR/EN language switcher with Django i18n
- **Reminder Command** — `python manage.py rappels_cours` to send course reminders via email
- **Admin Interface** — Django admin configured for all models

## Models

| Model        | Description                              |
|-------------|------------------------------------------|
| `Formation`  | Name, duration, description              |
| `Formateur`  | First name, last name, email, specialty  |
| `Etudiant`   | Personal info, associated course         |
| `Absence`    | Student, date, justification, status     |
| `Notification` | Message, channel (in-app/email/sms), date, read status |

## Installation

```bash
git clone <your-repo-url>
cd projets_django
python -m venv env
source env/bin/activate
pip install django twilio
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Configuration

### Email (Gmail)
Set these in `settings.py`:
```
EMAIL_HOST_USER = 'your.email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### SMS (Twilio — optional)
```
TWILIO_ACCOUNT_SID = 'your_sid'
TWILIO_AUTH_TOKEN = 'your_token'
TWILIO_PHONE_NUMBER = '+212XXXXXXX'
```

## Usage

1. Visit `http://127.0.0.1:8000/` for the homepage
2. Manage data at `http://127.0.0.1:8000/admin/`
3. Send course reminders: `python manage.py rappels_cours`

## Stack

- **Django 5.x** — Web framework
- **SQLite** — Database
- **Tailwind CSS** — Frontend
- **Twilio** — SMS (optional)
- **Gmail SMTP** — Email
