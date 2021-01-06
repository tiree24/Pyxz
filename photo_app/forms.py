from django import forms
from photo_app.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'photo', 'description', 'tags', 'is_story')