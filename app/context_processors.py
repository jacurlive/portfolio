from app.models import About


def about(request):
    return {
        "about": About.objects.first()
    }
