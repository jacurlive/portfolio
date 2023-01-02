from django.views.generic import TemplateView, ListView

from app.models import About


class MainView(ListView):
    template_name = 'index.html'
    queryset = About.objects.first()
    context_object_name = 'about'


class InnerView(TemplateView):
    template_name = 'inner-page.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio-details.html'

