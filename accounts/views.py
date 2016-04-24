from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Signup(CreateView):
    """User Signup"""
    model = User
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('login')
