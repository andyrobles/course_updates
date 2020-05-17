from django import forms
from .models import Course

class CreateAccountForm(forms.Form):
    username=forms.CharField(label='Username', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        }
    ))
    password=forms.CharField(label='Password', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'type': 'password'
        }
    ))
    confirm_password=forms.CharField(label='Confirm password', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'type': 'password'
        }
    ))

class SignInForm(forms.Form):
    username=forms.CharField(label='Username', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        }
    ))
    password=forms.CharField(label='Password', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'type': 'password'
        }
    ))

class AddCourseForm(forms.Form):
    course_reference_number=forms.CharField(label="CRN", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))

class RemoveCourseForm(forms.Form):
    course = forms.ModelChoiceField(label="Course", queryset=Course.objects.none(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))


    

