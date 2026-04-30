# gunicorn.conf.py — Gunicorn конфигурациясы
#
# Іске қосу командасы:
#   gunicorn --config gunicorn.conf.py myproject.wsgi:application

# Неше жұмысшы процесс (CPU саны × 2 + 1)
workers = 3

# Байланыс нүктесі (Nginx осы порттан сұраныс жібереді)
bind = '127.0.0.1:8000'

# Лог файлдары
accesslog = '/var/log/gunicorn/access.log'
errorlog  = '/var/log/gunicorn/error.log'
loglevel  = 'info'

# Сұраныс таймауты (секунд)
timeout = 30
keepalive = 2

# Жұмысшы класс (асинхронды үшін: gevent немесе uvicorn.workers.UvicornWorker)
worker_class = 'sync'
