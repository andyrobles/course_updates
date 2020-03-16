from django import forms

class AccountForm(forms.Form):
    email=forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        }
    ))
    password=forms.CharField(label='Password', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        }
    ))

class CourseForm(forms.Form):
    course_reference_number=forms.IntegerField(label="CRN", required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
        }
    ))
