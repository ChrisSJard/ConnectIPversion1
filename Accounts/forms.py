from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, PatentSummary


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # when form validates it creates new user
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ProfileInfoForm(forms.ModelForm):
    qualification = forms.CharField(max_length=100)
    research = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ['qualification', 'research', 'location']


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class PatentSummaryForm(forms.ModelForm):
    class Meta:
        model = PatentSummary
        fields = ['startDate',
                  'ad1', 'ad2', 'ad3', 'ad4', 'ad5',
                  'pr1', 'pr2', 'pr3', 'pr4', 'pr5', 'pr6', 'pr7', 'pr8', 'pr9',
                  'tech1', 'tech2', 'tech3', 'tech4',
                  'dev1', 'dev2', 'dev3',
                  'comp1', 'comp2', 'comp3', 'comp4', 'comp5', 'comp6', 'comp7',
                  'val1', 'val2', 'val3',
                  'endtime', 'exp', 'feedback',
                 ]
