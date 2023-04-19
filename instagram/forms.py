from django import forms
from . models import Instagram


class InstagramForm(forms.ModelForm):
    instagram_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Instagram
        fields = ("instagram_username", "instagram_password")


