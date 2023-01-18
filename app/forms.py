from django.forms import ModelForm

from app.models import Message


class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'email', 'subject', 'message')
