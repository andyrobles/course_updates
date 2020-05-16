from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .forms import AddCourseForm, RemoveCourseForm
from .models import Course

from courses.utilities import CourseSnapshot, FunctionLoop

@login_required
def index(request):
	# Update course status and seating availability if it has changed on course website
	for course_model in Course.objects.filter(user=request.user):
		course_snapshot = CourseSnapshot(course_model.crn)
		if course_snapshot_changed(course_snapshot, course_model):
			course_model.status = course_snapshot.status
			course_model.seating_availability = course_snapshot.seating_availability
			course_model.save()
	
	# Render most up to date courses
	return render(request, 'courses/index.html', {'course_list': Course.objects.filter(user=request.user)})

def course_snapshot_changed(course_snapshot, course_model):
	return course_snapshot.status != course_model.status and course_snapshot.seating_availability != course_model.seating_availability

@login_required
def add_course(request):
	if request.method == 'POST':
		# Get submitted course form
		course_form = AddCourseForm(request.POST)

		if course_form.is_valid():
			# Get snapshot of course specified by user by CRN
			course_snapshot = CourseSnapshot(course_form.cleaned_data['course_reference_number'])

			# Create a course with attributes identical to snapshot

			identical_courses = Course.objects.filter(user=request.user, crn=course_snapshot.crn)

			if len(identical_courses) >= 1:
				return render(request, 'components/dialogue.html', {
					'close_url': reverse('courses:index'),
					'background_template': 'courses/index.html',
					'course_list': Course.objects.filter(user=request.user),
					'subject': 'Duplicate Course',
					'icon': 'exclamation-triangle',
					'message': 'Course with this CRN already exists on watch list'
				})

			course = Course(
				user=request.user,
				crn=course_snapshot.crn,
				title=course_snapshot.title,
				instructor=course_snapshot.instructor,
				meeting_time=course_snapshot.meeting_time,
				location=course_snapshot.location,
				status=course_snapshot.status,
				seating_availability=course_snapshot.seating_availability,
			)

			course.save()
			
			return redirect(reverse('courses:index'))
			
		else:
			# Return error message if invalid form
			return render(request, 'components/dialogue.html', {
				'close_url': reverse('courses:index'),
				'background_template': 'courses/index.html',
				'course_list': Course.objects.filter(user=request.user),
				'subject': 'Try Again',
				'icon': 'exclamation-triangle',
				'message': 'Form contained one or more invalid fields'
			})

	# Render create course form if a get request
	return render(request, 'components/dialogue.html', {
		'close_url': reverse('courses:index'),
		'background_template': 'courses/index.html',
		'course_list': Course.objects.filter(user=request.user),
		'form': AddCourseForm(),
		'icon': 'graduation-cap',
		'subject': 'Add Course'
	})

@login_required
def remove_course(request):
	if request.method == 'POST':
		# Get submitted form form user when request method is post
		form = RemoveCourseForm(request.POST)
		form.fields['course'].queryset=Course.objects.filter(user=request.user)
			

		if form.is_valid():
			# Get selected course from user and delete it
			course = form.cleaned_data['course']
			course.delete()

			return redirect(reverse('courses:index'))

		# Return error form when form is invalid
		return render(request, 'components/dialogue.html', {
			'close_url': reverse('courses:index'),
			'background_template': 'courses/index.html',
			'course_list': Course.objects.filter(user=request.user),
			'icon': 'exclamation-triangle',
			'subject': 'Try Again',
			'message': 'Submitted form was invalid'
		})

	remove_course_form = RemoveCourseForm()
	remove_course_form.fields['course'].queryset=Course.objects.filter(user=request.user)
			
	# Return blank remove coures form when request method is get
	return render(request, 'components/dialogue.html', {
		'close_url': reverse('courses:index'),
		'background_template': 'courses/index.html',
		'course_list': Course.objects.filter(user=request.user),
		'form': remove_course_form,
		'icon': 'trash',
		'subject': 'Remove Course'
	})


