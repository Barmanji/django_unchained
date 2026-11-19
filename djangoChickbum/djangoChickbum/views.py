from django.http import JsonResponse


def health(request):
    """Liveness probe used by hosting platforms and uptime checks."""
    return JsonResponse({"status": "ok"})
