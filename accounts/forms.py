from django import forms

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