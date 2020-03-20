from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CreateAccountForm, SignInForm, CourseForm
from watcher.vcccd import CourseSnapshot
from .models import Course

def require_sign_in(view_function):
	def wrapped_view_function(request):
		if not request.user.is_authenticated:
			return redirect('sign_in')
		return view_function(request)
	return wrapped_view_function

def landing(request):
	return render(request, 'watcher/landing.html')

@require_sign_in
def index(request):
	return render(request, 'watcher/index.html')

def create_account(request):
	if request.method == 'POST':
		# Get submitted create account form
		create_account_form = CreateAccountForm(request.POST)

		if create_account_form.is_valid():
			# Tell user to try again if confirm password does not match
			if create_account_form.cleaned_data['password'] != create_account_form.cleaned_data['confirm_password']:
				return render(request, 'watcher/landing_modal.html', {
					'modal_title': 'Try Again',
					'icon': 'exclamation-triangle',
					'message': 'Password and Confirm password fields do not match'
				})

			# Create a user with the supplied email and password
			user = User.objects.create_user(
				username=create_account_form.cleaned_data['email'],
				password=create_account_form.cleaned_data['password']
			)

			# Redirect to index page
			return redirect('index')
		
		# Return error message if invalid form
		return render(request, 'watcher/landing_modal.html', {
			'modal_title': 'Try Again',
			'icon': 'exclamation-triangle',
			'message': 'Form contained one or more invalid fields'
		})

	# Render create account form if a get request		
	return render(request, 'watcher/landing_modal.html', {
		'form': CreateAccountForm(),
		'icon': 'user-plus',
		'modal_title': 'Create Account'
	})

def sign_in(request):
	if request.method == 'POST':
		# Get form from post request
		sign_in_form = SignInForm(request.POST)

		if sign_in_form.is_valid():
			# Authenticate user with form data
			user = authenticate(
				username=sign_in_form.cleaned_data['email'],
				password=sign_in_form.cleaned_data['password']
			)

			if user is not None:
				# Login authenticated user
				login(request, user)

				# Redirect to index
				return redirect('index')

			# Return an invalid login error message
			return render(request, 'watcher/landing_modal.html', {
				'icon': 'exclamation-triangle',
				'modal_title': 'Try Again',
				'message': 'Username or password were incorrect'
			})
		else:
			# Tell user to try again if form was invalid
			return render(request, 'watcher/landing_modal.html', {
				'icon': 'exclamation-triangle',
				'modal_title': 'Try Again',
				'message': 'Form contained one or more invalid fields'
			})

	# Provide user a blank sign in form
	return render(request, 'watcher/landing_modal.html', {
		'form': SignInForm(),
		'icon': 'sign-in-alt',
		'modal_title': 'Sign In'
	})

@require_sign_in
def add_course(request):
	if request.method == 'POST':
		# Get submitted course form
		course_form = CourseForm(request.POST)

		if course_form.is_valid():
			# Get snapshot of course specified by user by CRN
			course_snapshot = CourseSnapshot(course_form.cleaned_data['course_reference_number'])

			# Create a course with attributes identical to snapshot
			course = Course(
				crn=course_snapshot.crn,
				title=course_snapshot.title,
				instructor=course_snapshot.instructor,
				meeting_time=course_snapshot.meeting_time,
				location=course_snapshot.location,
				status=course_snapshot.status,
				waitlist_availability=course_snapshot.waitlist_availability
			)

			course.save()
			
			return redirect('index')
			
		else:
			# Return error message if invalid form
			return render(request, 'watcher/index_modal.html', {
				'modal_title': 'Try Again',
				'icon': 'exclamation-triangle',
				'message': 'Form contained one or more invalid fields'
			})

	# Render create course form if a get request
	return render(request, 'watcher/index_modal.html', {
		'form': CourseForm(),
		'icon': 'graduation-cap',
		'modal_title': 'Add Course'
	})

def sign_out(request):
	# Sign out whichever user is currently signed in
	logout(request)

	# Redirect to landing page
	return redirect('landing')
