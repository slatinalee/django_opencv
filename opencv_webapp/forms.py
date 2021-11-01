from django import forms
from .models import ImageUploadModel


class SimpleUploadForm(forms.Form):

    title = forms.CharField(max_length=50)
    image = forms.ImageField()
    # -> <input type="file" name='image' reqired id='image'>


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = ImageUploadModel
        fields = ('description', 'document',)
