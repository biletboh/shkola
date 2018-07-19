from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    """Render Support Contact form."""

    name = forms.CharField(label=_("Ім'я"), max_length=100, required=True)
    email = forms.EmailField(label=_('Емейл'), max_length=100, required=True)
    phone = forms.CharField(label=_('Телефон'), max_length=30, required=True)
    message = forms.CharField(label=_('Повідомлення'), max_length=512,
                              widget=forms.Textarea(), required=True)
