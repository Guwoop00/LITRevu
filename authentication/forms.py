from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from typing import Any


class LoginForm(AuthenticationForm):
    """Form for user login."""

    username: forms.CharField = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password: forms.CharField = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )


class SignupForm(UserCreationForm):
    """Form for user registration."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize form."""
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password1'].widget.attrs.update({'autocomplete': 'new-password', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'autocomplete': 'new-password',
                                                      'placeholder': 'Confirm Password'})

    class Meta(UserCreationForm.Meta):
        """Meta class for SignupForm."""
        model: Any = get_user_model()
