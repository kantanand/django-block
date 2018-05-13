import logging
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import User

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.utils import jwt_decode_handler

logger = logging.getLogger(__name__)


class MediaUrlsAuthMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any media content.
    """
    def process_request(self, request):
        if '/media' in request.path_info:
            jwt_auth = JSONWebTokenAuthentication()
            jwt_token = jwt_auth.get_jwt_value(request)
            if jwt_token:
                user_details = jwt_decode_handler(jwt_token)
                if user_details:
                    request.user = User.objects.get(
                        username=user_details['username'])
                    logger.info(
                        "[User-{0}-id-{1}] authenticated for media file {2}".format(
                            request.user.username, request.user.id, request.path_info
                        ))
