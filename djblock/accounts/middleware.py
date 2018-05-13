# -*- coding: UTF-8 -*-

# django dependencies
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.middleware import get_user
from django.conf import settings
from django.utils.functional import SimpleLazyObject
from django.utils.deprecation import MiddlewareMixin

# logging
import logging
logger = logging.getLogger(__name__)

# python dependencies
from re import compile

# JWT AUTH
from rest_framework.request import Request
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]

if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

def get_user_jwt(request):
    """
    get user from session or jwt headers 
    ref: https://github.com/GetBlimp/django-rest-framework-jwt/issues/45
    """
    user = get_user(request)
    if user.is_authenticated:
        return user
    try:
        user_jwt = JSONWebTokenAuthentication().authenticate(Request(request))
        if user_jwt is not None:
            return user_jwt[0]
    except:
        pass
    return user

class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """
    def process_request(self, request):
        assert hasattr(request, 'user'), "The Login Required middleware\
         requires authentication middleware to be installed. Edit your\
         MIDDLEWARE_CLASSES setting to insert\
         'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't\
         work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
         'django.core.context_processors.auth'."
        # get the user from the request
        request.user = SimpleLazyObject(lambda: get_user_jwt(request))

        # USED in ELB Testing --------------------
        ip = None
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        EXEMPT_PATH = "/server_health/"
        if request.get_full_path() != EXEMPT_PATH:
            logger.info("-------------------------------------------------")
            logger.info('path:' + str(request.get_full_path()))
            logger.info('auth header: ' + str(request.META.get('HTTP_AUTHORIZATION')))
            logger.info('user: ' + str(request.user) +' ip:'+str(ip))
            logger.info("-------------------------------------------------")
        # ----------------------------------------
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                path = request.get_full_path()
                return redirect_to_login(path, settings.LOGIN_URL, REDIRECT_FIELD_NAME)
