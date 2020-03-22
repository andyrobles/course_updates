from django import forms
from .models import Course

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
    

