from django.core.exceptions import ValidationError
from typing import Optional, Any


class ContainsLetterValidator:
    """Validator to check if a password contains at least one letter."""

    def validate(self, password: str, user: Optional[Any] = None) -> None:
        """Validate the password."""
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')

    def get_help_text(self) -> str:
        """Return the help text."""
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'


class ContainsNumberValidator:
    """Validator to check if a password contains at least one number."""

    def validate(self, password: str, user: Optional[Any] = None) -> None:
        """Validate the password."""
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir un chiffre', code='password_no_number')

    def get_help_text(self) -> str:
        """Return the help text."""
        return 'Votre mot de passe doit contenir au moins un chiffre.'
