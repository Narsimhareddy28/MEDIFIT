from django import forms

from problems.models import Problems
from diet.models import Diet


class UserProfileForm(forms.Form):
    height = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Height in cm'}))
    weight = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Weight in kg'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Date of Birth', 'type': 'date'}))


CHOICES = [('Male', 'Male'), ('Female', 'Female')]
CHOICES_EXERCISE = [('0', 'Little or no exercise'),
                    ('1', 'Exercise 1-3 days/week'),
                    ('2', 'Exercise 3-5 days/week'),
                    ('3', 'Exercise 6 days/week'),
                    ('4', 'Hard exercise on all 7 days')]


class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    emailId = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    f_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    l_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    height = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Height in cm'}))
    weight = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Weight in kg'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Date of Birth', 'type': 'date'}))
    medical_conditions = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                        queryset=Problems.objects.all())
    gender = forms.CharField(widget=forms.RadioSelect(choices=CHOICES, attrs={'placeholder': 'Gender'}), label="Gender")
    diet = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                          queryset=Diet.objects.all())
    exercise_frequency = forms.CharField(widget=forms.RadioSelect(choices=CHOICES_EXERCISE), label="exercise_frequency")



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
