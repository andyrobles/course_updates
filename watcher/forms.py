from django import forms
from .models import Course

class CreateAccountForm(forms.Form):
    email=forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
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
    email=forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
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
    course=forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))
    

