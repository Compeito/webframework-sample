from .http import http405


def require_http_methods(methods):
    def decorator(view):
        def _wrapped_view(request, *args, **kwargs):
            if request.method in [m.upper() for m in methods]:
                return view(request, *args, **kwargs)
            else:
                return http405(request)

        return _wrapped_view

    return decorator


require_GET = require_http_methods(['GET'])
require_POST = require_http_methods(['POST'])
