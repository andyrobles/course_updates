from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CreateAccountForm, SignInForm, CourseForm

def landing(request):
	return render(request, 'watcher/landing.html')

def index(request):
	return render(request, 'watcher/index.html')

def create_account(request):
	if request.method == 'POST':
		# Get submitted create account form
		create_account_form = CreateAccountForm(request.POST)

		if create_account_form.is_valid():
			# Get user entered data from the form
			email = create_account_form.cleaned_data['email']
			password = create_account_form.cleaned_data['password']
			confirm_password = create_account_form.cleaned_data['confirm_password']

			# Tell user to try again if confirm password does not match
			if password != confirm_password:
				return render(request, 'watcher/landing_modal.html', {
					'modal_title': 'Try Again',
					'icon': 'exclamation-triangle',
					'message': 'Password and Confirm password fields do not match'
				})

			# Create a user with the supplied email and password
			user = User.objects.create_user(
				create_account_form.cleaned_data['email'],
				create_account_form.cleaned_data['password']
			)

			# Redirect to landing page
			return redirect('landing')
		
		else:
			# Return error message if invalid form
			return render(request, 'watcher/landing_modal.html', {
				'modal_title': 'Try Again',
				'icon': 'exclamation-triangle',
				'message': 'Form contained one or more invalid fields'
			})

	else:
		# Render create account form if a get request		
		return render(request, 'watcher/landing_modal.html', {
			'form': CreateAccountForm(),
			'icon': 'user-plus',
			'modal_title': 'Create Account'
		})

def sign_in(request):
	return render(request, 'watcher/landing_modal.html', {
		'form': SignInForm(),
		'icon': 'sign-in-alt',
		'modal_title': 'Sign In'
	})

def add_course(request):
	return render(request, 'watcher/index_modal.html', {
		'form': CourseForm(),
		'icon': 'graduation-cap',
		'modal_title': 'Add Course'
	})

def sign_out(request):
	return redirect('landing')
		
