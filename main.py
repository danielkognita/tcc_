

from myapp.forms import DocumentForm
from myapp.models import Document

from django.core.wsgi import get_wsgi_application

# Este arquivo 'main.py' é o ponto de entrada do seu aplicativo.
# Ele é usado pelo Gunicorn para iniciar o servidor web.

# Obtém a instância do aplicativo Django.
application = get_wsgi_application()
