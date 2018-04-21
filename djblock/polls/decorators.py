from django.core.exceptions import PermissionDenied
from polls.models import Question


def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):
        entry = Question.objects.filter(pk=kwargs['question_id']).first()
        if entry.created_by == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
