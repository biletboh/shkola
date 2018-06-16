from django import forms
from django.utils.translation import gettext as _

from django_file_form.forms import UploadedFileField

from core.mixins import CustomFileFormMixin
from theteachers.models import Teacher


class TeacherModelForm(CustomFileFormMixin, forms.ModelForm):
    """Render a Post model form."""

    image = UploadedFileField(label=_('Світлина'), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['image'].initial = self.instance.image

    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'information', 'slug')
        widgets = {
            'information': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        image = self.cleaned_data['image']
        instance.image = image
        if commit:
            instance.save()

        self.delete_temporary_files()
        return instance
