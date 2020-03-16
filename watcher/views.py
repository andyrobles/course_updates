from django.shortcuts import render, redirect
from .forms import AccountForm, CourseForm 

def landing(request):
	return render(request, 'watcher/landing.html')

def index(request):
	return render(request, 'watcher/index.html')

def create_account(request):
	return render(request, 'watcher/form.html', {
		'form': AccountForm(),
		'icon': 'user-plus',
		'modal': 'Create Account'
	})

def sign_in(request):
	return render(request, 'watcher/form.html', {
		'form': AccountForm(),
		'icon': 'sign-in-alt',
		'modal': 'Sign In'
	})

def add_course(request):
	return render(request, 'watcher/form.html', {
		'form': CourseForm(),
		'icon': 'graduation-cap',
		'modal': 'Add Course'
	})

def sign_out(request):
	return redirect('landing')
		
