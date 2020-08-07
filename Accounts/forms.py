from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.widgets import CountrySelectWidget
from .models import Profile, PatentSummary


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # when form validates it creates new user
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['qualification', 'research', 'location']
        widgets = {'location': CountrySelectWidget()}


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class AdministrativeInformationForm(forms.ModelForm):
    class Meta:
        model = PatentSummary
        fields = ['startDate', 'ad1', 'ad2', 'ad3', 'ad4', 'ad5']
        labels = {
            'ad1': 'Technology Title', 'ad2': 'Year Patented', 'ad3': 'Patent Status', 'ad4': 'Institution',
            'ad5': 'Patent link',
        }
        widgets = {'startDate': DateInput()}


class ProductMarketSpeculationForm(forms.ModelForm):
    class Meta:
        model = PatentSummary
        fields = ['pr1', 'pr2', 'pr3', 'pr4', 'pr5', 'pr6', 'pr7', 'pr8', 'pr9']
        labels = {
            'pr1': 'In two sentences or less, articulate the problem in your own words in layman terms.',
            'pr2': 'Rate your perceived difficulty of articulating the problem.',
            'pr3': 'In two sentences or less, articulate the solution in your own words in layman terms.',
            'pr4': 'Rate your perceived difficulty of articulating the solution.',
            'pr5': 'Who will this help directly?',
            'pr6': 'How many of these people exist today?',
            'pr7': 'How many new people will this help next year',
            'pr8': 'Who are indirect winners?',
            'pr9': 'What is the value added by this technology overall?',
        }
        widgets = {'pr2': forms.RadioSelect, 'pr4': forms.RadioSelect}


class CharacterizingTechnologyForm(forms.ModelForm):
    class Meta:
        model = PatentSummary
        fields = ['tech1', 'tech2', 'tech3', 'tech4']
        labels = {
            'tech1': 'Category', 'tech2': 'What features does this technology have?',
            'tech3': 'How does it work (with scientific jargon)?',
            'tech4': 'How does it work (without scientific jargon)?',
        }


class StageDevelopmentForm(forms.ModelForm):
    class Meta:
        model = PatentSummary
        fields = ['dev1', 'dev2', 'dev3']
        labels = {
            'dev1': 'Technology Readiness Level',
            'dev2': 'Justify your choice',
            'dev3': 'What is one logical next step to move it forward?',
        }


class CompetitiveLandscapeForm(forms.ModelForm):
    class Meta:
        model = PatentSummary
        fields = ['comp1', 'comp2', 'comp3', 'comp4', 'comp5', 'comp6', 'comp7']
        labels = {
            'comp1': 'Are there any commercially available products that target the problem this invention is designed to solve?',
            'comp2': 'Are there other patents that suggest a solution to solve this problem?',
            'comp3': 'Is there ongoing commercial research that targets the problem this technology is designed to solve?',
            'comp4': 'Who will lose if this technology becomes commercially available?',
            'comp5': 'Do the current solutions completely solve the problem for the people you identified previously?',
            'comp6': 'Will this be a first-in-class/groundbreaking product or a rox improvement?',
            'comp7': 'Will this improve the cost-effectiveness of addressing this problem or lead to cost-savings?',
        }


class ValidationForm(forms.ModelForm):
    class Meta:
        model = PatentSummary
        fields = ['val1', 'val2', 'val3']
        labels = {
            'val1': 'Scientific basis', 'val2': 'Reproducibility', 'val3': 'References'
        }


class PostSurveyForm(forms.ModelForm):
    class Meta:
        model = PatentSummary
        fields = ['endtime', 'exp', 'feedback']
        labels = {
            'endtime': 'Completion date',
            'exp': 'How was your experience?',
            'feedback': 'Note any feedback to improve form',
        }
        widgets = {'endtime': DateInput(), 'exp': forms.RadioSelect}


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
        labels = {
            'ad1': 'Technology Title', 'ad2': 'Year Patented', 'ad3': 'Patent Status', 'ad4': 'Institution',
            'ad5': 'Patent link',
            'pr1': 'In two sentences or less, articulate the problem in your own words in layman terms.',
            'pr2': 'Rate your perceived difficulty of articulating the problem.',
            'pr3': 'In two sentences or less, articulate the solution in your own words in layman terms.',
            'pr4': 'Rate your perceived difficulty of articulating the solution.',
            'pr5': 'Who will this help directly?',
            'pr6': 'How many of these people exist today?',
            'pr7': 'How many new people will this help next year',
            'pr8': 'Who are indirect winners?',
            'pr9': 'What is the value added by this technology overall?',
            'tech1': 'Category', 'tech2': 'What features does this technology have?',
            'tech3': 'How does it work (with scientific jargon)?',
            'tech4': 'How does it work (without scientific jargon)?',
            'dev1': 'Technology Readiness Level', 'dev2': 'Justify your choice',
            'dev3': 'What is one logical next step to move it forward?',
            'comp1': 'Are there any commercially available products that target the problem this invention is designed to solve?',
            'comp2': 'Are there other patents that suggest a solution to solve this problem?',
            'comp3': 'Is there ongoing commercial research that targets the problem this technology is designed to solve?',
            'comp4': 'Who will lose if this technology becomes commercially available?',
            'comp5': 'Do the current solutions completely solve the problem for the people you identified previously?',
            'comp6': 'Will this be a first-in-class/groundbreaking product or a rox improvement?',
            'comp7': 'Will this improve the cost-effectiveness of addressing this problem or lead to cost-savings?',
            'val1': 'Scientific basis', 'val2': 'Reproducibility', 'val3': 'References',
            'endtime': 'Completion date', 'exp': 'How was your experience?',
            'feedback': 'Note any feedback to improve form',
        }
