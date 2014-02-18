from django import forms
from kata.models import Media

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['file']

class MediaSimpleForm(forms.Form):
    file = forms.FileField()    