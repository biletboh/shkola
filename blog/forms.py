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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image
        self.fields['pub_date'].input_formats = ['%d-%m-%Y %H:%M']
        if not self.instance.pub_date:
            self.fields['pub_date'].initial = timezone.now().strftime(
                                                             '%d-%m-%Y %H:%M')

    class Meta:
        model = Post
        fields = ('title', 'body', 'short_descr', 'pub_date', 'slug')
        widgets = {
            'short_descr': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
            'body': TinyMCE(attrs={'cols': 80, 'rows': 20}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data['image']
        instance.image = image
        if commit:
            instance.save()

        self.delete_temporary_files()
        return instance
