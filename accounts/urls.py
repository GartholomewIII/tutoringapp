from django.urls import path
from .views import SignUpView

url_patterns = [
    path("signup/", SignUpView.as_view(), name="signup")
]