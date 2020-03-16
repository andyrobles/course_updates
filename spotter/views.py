from django.shortcuts import render
from .forms import AccountForm, CourseForm 

def index(request):
	return render(request, 'spotter/index.html')

def create_account(request):
	return render(request, 'spotter/form.html', {
		'form': AccountForm(),
		'icon': 'user-plus',
		'modal': 'Create Account'
	})

def sign_in(request):
	return render(request, 'spotter/form.html', {
		'form': AccountForm(),
		'icon': 'sign-in-alt',
		'modal': 'Sign In'
	})

def add_course(request):
	return render(request, 'spotter/form.html', {
		'form': CourseForm(),
		'icon': 'graduation-cap',
		'modal': 'Add Course'
	})
		
