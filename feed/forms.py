from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput
from feed.models import Member


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'register-form'}), required=True)
    # last_name = forms.CharField(required=True)
    bio = forms.CharField(widget=forms.Textarea(attrs={'cols': 36, 'rows': 3}))

    class Meta:
        model = Member
        fields = ("username", "first_name", "last_name", "bio", "profile_photo", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Member.objects.get(username=username)
        except Member.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )
