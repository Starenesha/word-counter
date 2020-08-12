from django import forms
from .models import Text


class TextInputForm(forms.ModelForm):
    # text = forms.CharField(label="Text input:", widget=forms.Textarea)
    class Meta:
        model = Text
        fields = ["text"]

        widgets = {
            'text': forms.Textarea()
        }
