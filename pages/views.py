from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from accounts.models import CustomUser


class HomePageView(TemplateView):
    model = CustomUser
    template_name = "home.html"
    context_object_name = "tutors"

