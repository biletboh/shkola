from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
from easy_thumbnails.fields import ThumbnailerImageField
from tinymce.models import HTMLField


class Teacher(models.Model):
    """Store information about a teacher."""

    first_name = models.CharField(_("Ім'я"), max_length=90)
    last_name = models.CharField(_('Прізвище'), max_length=90)
    information = HTMLField(_('Інформація'), max_length=500, blank=True)
    pub_date = models.DateTimeField(_('Дата публікації'), default=timezone.now)
    image = ThumbnailerImageField(_('Світлина'), upload_to='photos/teachers',
                                  blank=True)
    slug = models.SlugField(_('Посилання'), unique=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'posts'
