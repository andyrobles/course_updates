from django import forms

class AccountForm(forms.Form):
    email=forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        }
    ))
    password=forms.CharField(label='Password', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        }
    ))
