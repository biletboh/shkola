from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from information.forms import ContactForm
from information.utils import send_message


class About(TemplateView):
    """Render About page."""

    template_name = 'information/about.html'


class Contacts(TemplateView):
    """Render Contacts page."""

    template_name = 'information/contacts.html'


class ContactFormView(SuccessMessageMixin, FormView):
    """Send message from contact form."""

    form_class = ContactForm
    template_name = 'information/contact_form.html'
    success_url = reverse_lazy('information:contact')
    success_message = _('Повідомлення надісланно!')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']
        send_message(name=name, email=email,
                     contact_message=message, phone=phone)
        return super().form_valid(form)
