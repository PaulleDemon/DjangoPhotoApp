from django import forms
from photoapp.models import PhotoModel


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ('photo_title', 'photo_description', 'photo')
