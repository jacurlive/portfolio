from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'index.html'


class InnerView(TemplateView):
    template_name = 'inner-page.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio-details.html'

