import os

from django.core.wsgi import get_wsgi_application
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()

# Configure o Django para usar as configurações do Google App Engine
if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
    # Adicione o suporte ao Django WhiteNoise para servir arquivos estáticos
    from whitenoise import WhiteNoise
    application = WhiteNoise(application)
    application.add_files(settings.STATIC_ROOT)
