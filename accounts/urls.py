from django.urls import path
from .views import HoursUpdateView, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("hours/", HoursUpdateView.as_view(), name="update_hours"),
]