from django.views.generic import TemplateView


class About(TemplateView):
    """Render About page."""

    template_name = 'information/about.html'


class Contacts(TemplateView):
    """Render Contacts page."""

    template_name = 'information/contacts.html'
