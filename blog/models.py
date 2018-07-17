from django.db import models
# from django.utils import timezone
from django.utils.translation import gettext as _
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField


class Post(models.Model):
    """Store post data for a blog."""

    title = models.CharField(_('Заголовок'), max_length=128)
    short_descr = HTMLField(_('Короткий опис'), max_length=256, blank=True)
    body = HTMLField(_('Текст'), blank=True)
    pub_date = models.DateTimeField(_('Дата публікації'))
    image = ThumbnailerImageField(
        _('Світлина'), upload_to='photos/blog', blank=True,
        default=('placeholder-post.jpg'))
    slug = models.SlugField(_('Посилання'), unique=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'posts'
