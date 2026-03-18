# Attendance Calculator Platform

This is a simple Django attendance calculator with one main page where a student can enter total classes and attended classes, then see:

- attendance percentage
- whether they are above or below the 75% threshold
- how many more classes they need to attend to recover

## Project Structure

```text
Attendance Calculator Platform/
|-- attendance_site/
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- calculator/
|   |-- migrations/
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
|-- templates/
|   `-- home.html
|-- manage.py
`-- requirements.txt
```

## Local Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run migrations:

```bash
python manage.py migrate
```

3. Start the development server:

```bash
python manage.py runserver
```

4. Open `http://127.0.0.1:8000/`

## Production Environment Variables

The app now supports these environment variables:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`

Examples:

```bash
DJANGO_SECRET_KEY=replace-this-with-a-long-random-value
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-app.onrender.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://your-app.onrender.com
DATABASE_URL=postgresql://user:password@host:5432/dbname
```

## Deploy on Render

Render is a good option if you want a public URL quickly.

1. Push this project to GitHub.
2. In Render, create a new PostgreSQL database.
3. Create a new Web Service and connect the repository.
4. Use this build command:

```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput
```

5. Use this start command:

```bash
gunicorn attendance_site.wsgi
```

6. Add these environment variables in Render:

```bash
DJANGO_SECRET_KEY=<your-secret-key>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=<your-render-domain>
DJANGO_CSRF_TRUSTED_ORIGINS=https://<your-render-domain>
DATABASE_URL=<your-render-postgres-url>
```

7. Deploy the service.

Important:

- Use `attendance_site.wsgi`, not `attendance_platform.wsgi`.
- Do not use SQLite on Render if you need persistent data. Render web service disks are not ideal for that workflow, so PostgreSQL is the safer choice.

## Deploy on PythonAnywhere

PythonAnywhere is simpler if you are okay with SQLite or a small personal deployment.

1. Upload the project.
2. Create a virtual environment and run:

```bash
pip install -r requirements.txt
```

3. In the web app configuration, set the WSGI entry point to:

```python
application = get_wsgi_application()
```

with `DJANGO_SETTINGS_MODULE` set to:

```bash
attendance_site.settings
```

4. Set environment variables:

```bash
DJANGO_SECRET_KEY=<your-secret-key>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=<your-pythonanywhere-domain>
DJANGO_CSRF_TRUSTED_ORIGINS=https://<your-pythonanywhere-domain>
```

5. Run:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

6. Reload the web app.

## Quick Deployment Checklist

- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py collectstatic --noinput`
- set `DJANGO_DEBUG=False`
- set `DJANGO_SECRET_KEY`
- set `DJANGO_ALLOWED_HOSTS`
- start with `gunicorn attendance_site.wsgi`
