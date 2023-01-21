from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.views.generic.edit import FormMixin

from app.forms import ContactForm
from app.models import Skill, Sumary, Education, About, Message, Project


class MainView(FormView, ListView):
    template_name = 'index.html'
    form_class = ContactForm
    queryset = About.objects.all()
    success_url = reverse_lazy('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['skill'] = Skill.objects.all()
        context['sumary'] = Sumary.objects.all()
        context['education'] = Education.objects.all()
        context['projects'] = Project.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class InnerView(TemplateView):
    template_name = 'inner-page.html'


class CustomDetailView(DetailView):
    template_name = 'portfolio-details.html'
    query_pk_and_slug = 'slug'
    queryset = Project.objects.all()
    context_object_name = 'project'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['']


class CustomSuccessView(TemplateView):
    template_name = 'success_contact.html'
