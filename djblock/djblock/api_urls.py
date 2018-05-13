from django.conf.urls import url
from django.urls import include, path
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='Pastebin API')

from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token


# Here you will write only api end points 
app_name = 'api'
urlpatterns = [
    url(r'^schema/$', schema_view),
    # JWT api urls 
    url(r'^get-auth-token/', obtain_jwt_token),
    url(r'^refresh-jwt-token/', refresh_jwt_token),
    url(r'^verify-jwt-token/', verify_jwt_token),
    # local apps url
    url(r'^polls/', include('polls.urls'), name='polls'),
    url(r'^accounts/', include('accounts.urls')),
]
