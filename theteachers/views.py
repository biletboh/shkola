from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DetailView,\
        DeleteView, ListView, UpdateView, CreateView

from theteachers.models import Teacher
from theteachers.forms import TeacherModelForm


class TeacherList(ListView):
    """Render List of posts."""

    model = Teacher
    context_object_name = 'teachers'
    template_name = 'theteachers/list.html'
    paginate_by = 10


class Page(DetailView):
    """Render Teacher Page."""

    model = Teacher
    template_name = 'theteachers/page.html'


class CreateTeacher(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create Teachers."""

    form_class = TeacherModelForm
    template_name = 'theteachers/create.html'
    success_url = reverse_lazy('theteachers:update_list')
    success_message = _('Учителя додано!')


class UpdateTeacher(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update a post."""

    model = Teacher
    form_class = TeacherModelForm
    template_name = 'theteachers/update.html'
    success_message = _('Iнформацію про учителя оновлено!')

    def get_success_url(self):
        return reverse_lazy('theteachers:update',
                            kwargs={'slug': self.object.slug})


class DeleteTeacher(LoginRequiredMixin, DeleteView):
    """Delete a Teacher."""

    model = Teacher
    success_url = reverse_lazy('theteachers:update_list')


class UpdateTeacherList(LoginRequiredMixin, ListView):
    """Render a list of Teachers to edit."""

    model = Teacher
    template_name = 'theteachers/update_list.html'
    context_object_name = 'teachers'
    paginate_by = 10
