web: gunicorn myproject.wsgi --bind 0.0.0.0:$PORT --worker-class gthread --threads 4 --timeout 1200
web: python manage.py runserver 
