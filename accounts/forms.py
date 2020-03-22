from django import forms

class CreateAccountForm(forms.Form):
    phone_number=forms.CharField(label='Phone Number', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '9 digits numbers only: XXXXXXXXX'
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
    phone_number=forms.CharField(label='Phone Number', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '9 digits numbers only: XXXXXXXXX'
        }
    ))
    password=forms.CharField(label='Password', required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'autocomplete': 'off',
            'type': 'password'
        }
    ))