from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from authentication.forms import SignupForm
from django.http import HttpRequest, HttpResponse


class CustomLoginView(LoginView):
    """Custom login view."""

    template_name = 'authentication/login.html'


def signup_page(request: HttpRequest) -> HttpResponse:
    """Sign up page view."""
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', {'form': form})
