from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

SUBJECTS = ["Math", "Physics", "Chemistry", "Biology", "Computer Science", "English"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
HOURS = [
    "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM",
    "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM",
    "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM",
]


def make_choices(values):
    return [(v, v) for v in values]


class CustomUserCreationForm(UserCreationForm):
    subjects = forms.MultipleChoiceField(
        choices=make_choices(SUBJECTS),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Courses you can tutor",
    )
    days = forms.MultipleChoiceField(
        choices=make_choices(DAYS),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Days available",
    )
    hours = forms.MultipleChoiceField(
        choices=make_choices(HOURS),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Times available",
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "subjects", "days", "hours")


class CustomUserChangeForm(UserChangeForm):
    subjects = forms.MultipleChoiceField(
        choices=make_choices(SUBJECTS),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    days = forms.MultipleChoiceField(
        choices=make_choices(DAYS),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    hours = forms.MultipleChoiceField(
        choices=make_choices(HOURS),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "subjects", "days", "hours")