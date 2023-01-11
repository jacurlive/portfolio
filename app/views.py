from django.views.generic import TemplateView, ListView, DetailView

from app.models import Skill, Sumary, Education


class MainView(ListView):
    template_name = 'index.html'
    queryset = Skill.objects.all()
    context_object_name = 'skill'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        # context['skill'] = Skill.objects.all()
        context['sumary'] = Sumary.objects.all()
        context['education'] = Education.objects.all()
        return context


class InnerView(TemplateView):
    template_name = 'inner-page.html'


class PortfolioView(ListView):
    template_name = 'portfolio-details.html'
    queryset = Skill.objects.all()

