from django.http import HttpResponseForbidden
from functools import wraps
from rest_framework.request import Request

def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request: Request, *args, **kwargs):
            if not hasattr(request.user, 'role') or request.user.role != required_role:
                return HttpResponseForbidden("You do not have permission to access this resource.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator