from django import forms
from django.utils import timezone
from django.utils.translation import gettext as _

from django_file_form.forms import UploadedFileField
from tinymce.widgets import TinyMCE

from core.mixins import CustomFileFormMixin
from blog.models import Post


class PostModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render a Post model form."""

    image = UploadedFileField(label=_('Світлина'), required=False)
    image_pl = UploadedFileField(label=_('Світлина польською'), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image
        if self.instance:
            self.fields['image_pl'].initial = self.instance.image_pl
        self.fields['pub_date'].input_formats = ['%d-%m-%Y %H:%M']
        if not self.instance.pub_date:
            self.fields['pub_date'].initial = timezone.now().strftime(
                                                             '%d-%m-%Y %H:%M')

    class Meta:
        model = Post
        fields = ('title', 'body', 'short_descr', 'title_pl', 'body_pl',
                  'short_descr_pl', 'pub_date', 'slug')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'short_descr_pl': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
            'body_pl': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data['image']
        image_pl = self.cleaned_data['image_pl']
        instance.image = image
        instance.image_pl = image_pl
        if commit:
            instance.save()

        self.delete_temporary_files()
        return instance
