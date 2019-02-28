from .response import Response


def http404(request):
    return Response(status=404)


def http405(request):
    return Response(status=405)
