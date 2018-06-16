from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView, ListView, UpdateView, CreateView

from hitcount.views import HitCountDetailView

from blog.models import Post
from blog.forms import PostModelForm


class PostList(ListView):
    """Render List of posts."""

    model = Post
    context_object_name = "posts"
    template_name = 'blog/blog.html'
    paginate_by = 10


class Page(HitCountDetailView):
    """Render Post Page."""

    model = Post
    count_hit = True
    template_name = 'blog/page.html'


class CreatePost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create Posts."""

    form_class = PostModelForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:update_list')
    success_message = _('Запис додано!')


class UpdatePost(LoginRequiredMixin, UpdateView):
    """Update a post."""

    model = Post
    form_class = PostModelForm
    template_name = 'blog/update.html'
    success_message = _('Запис оновлено!')

    def get_success_url(self):
        return reverse_lazy('blog:update', kwargs={'slug': self.object.slug})


class DeletePost(LoginRequiredMixin, DeleteView):
    """Delete a Post."""

    model = Post
    success_url = reverse_lazy('blog:update_list')


class UpdatePostList(LoginRequiredMixin, ListView):
    """Render a list of Posts to edit."""

    model = Post
    template_name = 'blog/update_list.html'
    context_object_name = 'posts'
    paginate_by = 20
