from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm
class cSignupForm(UserCreationForm):

    email=forms.EmailField(label="email")
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
            "email",
        )