from django.shortcuts import render
from .forms import AccountForm 

def index(request):
	return render(request, 'spotter/index.html')

def create_account(request):
	return render(request, 'spotter/form.html', {
		'form': AccountForm(),
		'icon': 'user-plus',
		'modal_title': 'Create Account'
	})
		
