from django import forms
from .models import Video


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video

        fields = ["title", "video"]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter Video Title"
                }
            ),
            "video": forms.FileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }