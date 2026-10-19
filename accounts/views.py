from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, HoursUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class HoursUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = HoursUpdateForm
    template_name = "hours_form.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user
