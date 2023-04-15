
from __future__ import unicode_literals

import django
from django.conf.urls import url
from django.contrib.auth import views

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

if django.VERSION < (1, 11):
    login = views.login
    login_kwargs = {'template_name': 'rest_framework/login.html'}
    logout = views.logout
else:
    login = views.LoginView.as_view(template_name='rest_framework/login.html')
    login_kwargs = {}
    logout = views.LogoutView.as_view()


app_name = 'rest_framework'



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', login, login_kwargs, name='login'),
    url(r'^logout/$', logout, name='logout'),
]