from django.shortcuts import render
from django.views.generic import DetailView, ListView
from accounts.models import CustomUser


class HomePageView(ListView):
    model = CustomUser
    template_name = "home.html"
    context_object_name = "tutors"


class TutorDetailView(DetailView):
    model = CustomUser
    template_name = "tutor_detail.html"
    context_object_name = "tutor"

