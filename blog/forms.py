from django.contrib.auth import get_user_model
from django import forms
from blog.models import UserFollows

User = get_user_model()


class FollowUserForm(forms.ModelForm):
    """
    Form to follow a user.
    """

    class Meta:
        model = UserFollows
        fields = ('followed_user',)
        labels = {
            "followed_user": 'Username',
        }

    def __init__(self, current_user, *args, **kwargs):
        """
        Initialize the form.

        Args:
            current_user: The currently logged-in user.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(*args, **kwargs)
        # Exclude the current user and users already followed by the current user
        q = User.objects.exclude(id=current_user.id).exclude(id__in=current_user.follows.all())
        self.fields['followed_user'].queryset = q
