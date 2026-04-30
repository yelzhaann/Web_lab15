# Lab 15 — Django Production Setup

Django жобасын өндірістік ортаға дайындау: `.env`, `DEBUG=False`, `ALLOWED_HOSTS`, `STATIC_ROOT`, Nginx/Gunicorn.

## Орнату

```bash
pip install -r requirements.txt
```

## .env файлын жасау

`.env.example` негізінде `.env` файлын жасаңыз:

```bash
cp .env.example .env
```

Содан кейін `.env` ішіне өз мәндеріңізді жазыңыз.

## Іске қосу

```bash
python manage.py migrate
python manage.py runserver
```

## Статикалық файлдарды жинау

```bash
python manage.py collectstatic
```
