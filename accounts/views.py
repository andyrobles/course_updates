from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import CreateAccountForm, SignInForm

def index(request):
    return render(request, 'accounts/index.html')

def create_account(request):
	if request.method == 'POST':
		# Get submitted create account form
		create_account_form = CreateAccountForm(request.POST)

		if create_account_form.is_valid() and is_valid_phone_number(create_account_form.cleaned_data['phone_number']):
			# Tell user to try again if confirm password does not match
			if create_account_form.cleaned_data['password'] != create_account_form.cleaned_data['confirm_password']:
				return render(request, 'components/dialogue.html', {
					'close_url': reverse('accounts:index'),
					'background_template': 'accounts/index.html',
					'subject': 'Try Again',
					'icon': 'exclamation-triangle',
					'message': 'Password and Confirm password fields do not match'
				})

			# Create a user with the supplied email and password
			user = User.objects.create_user(
				username=create_account_form.cleaned_data['phone_number'],
				password=create_account_form.cleaned_data['password']
			)

			# Authenticate user that we just created  
			login(request, user)

			# Redirect to index page
			return redirect(reverse('courses:index'))
		
		# Return error message if invalid form
		return render(request, 'components/dialogue.html', {
			'close_url': reverse('accounts:index'),
			'background_template': 'accounts/index.html',
			'subject': 'Try Again',
			'icon': 'exclamation-triangle',
			'message': 'Form contained one or more invalid fields'
		})

	# Render create account form if a get request		
	return render(request, 'components/dialogue.html', {
		'close_url': reverse('accounts:index'),
		'background_template': 'accounts/index.html',
		'form': CreateAccountForm(),
		'icon': 'user-plus',
		'subject': 'Create Account'
	})

def sign_in(request):
	if request.method == 'POST':
		# Get form from post request
		sign_in_form = SignInForm(request.POST)

		if sign_in_form.is_valid() and is_valid_phone_number(sign_in_form.cleaned_data['phone_number']):
			# Authenticate user with form data
			user = authenticate(
				username=sign_in_form.cleaned_data['phone_number'],
				password=sign_in_form.cleaned_data['password']
			)

			if user is not None:
				# Login authenticated user
				login(request, user)

				# Redirect to index
				return redirect(reverse('courses:index'))

			# Return an invalid login error message
			return render(request, 'components/dialogue.html', {
				'close_url': reverse('accounts:index'),
				'background_template': 'accounts/index.html',
				'icon': 'exclamation-triangle',
				'subject': 'Try Again',
				'message': 'Username or password were incorrect'
			})
		else:
			# Tell user to try again if form was invalid
			return render(request, 'components/dialogue.html', {
				'close_url': reverse('accounts:index'),
				'background_template': 'accounts/index.html',
				'icon': 'exclamation-triangle',
				'subject': 'Try Again',
				'message': 'Form contained one or more invalid fields'
			})

	# Provide user a blank sign in form
	return render(request, 'components/dialogue.html', {
		'close_url': reverse('accounts:index'),
		'background_template': 'accounts/index.html',
		'form': SignInForm(),
		'icon': 'sign-in-alt',
		'subject': 'Sign In'
	})

def is_valid_phone_number(string_value):
	return len(string_value) == 10 and string_value.isdigit()

def sign_out(request):
	# Sign out whichever user is currently signed in
	logout(request)

	# Redirect to landing page
	return redirect(reverse('accounts:index'))