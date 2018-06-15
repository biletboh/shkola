from django_file_form.forms import FileFormMixin
from django import forms


class CustomFileFormMixin(FileFormMixin):
    form_id = forms.CharField(widget=forms.HiddenInput(), required=False)
    upload_url = forms.CharField(widget=forms.HiddenInput(), required=False)
    delete_url = forms.CharField(widget=forms.HiddenInput(), required=False)
