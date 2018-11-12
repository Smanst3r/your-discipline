from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import transaction
from .models import *
from .forms import FacultyForm, SpecializationForm, ChooseDisciplineForm

@login_required
def home(request):
	faculty = Faculty.objects.all()
	specs = Specialization.objects.all()
	
	# loggedUser = authenticate(username=request.user.username, password=request.user.password)
	# if not loggedUser:
	# 	return redirect('login')

	return render(request, 'service/home.html', {'faculty': faculty, 'specs': specs})
			
def faculty(request):
	if request.method == "POST":
		form = FacultyForm(request.POST)
		if form.is_valid():
			return redirect('specialization')
	else:
		form = FacultyForm()
	_faculty = Faculty.objects.all()
	return render(request, 'service/faculty.html', {'faculty': _faculty, 'form': form})

def specialization(request, pk):
	specialization = Specialization.objects.filter(faculty=pk)
	disciplines = Discipline.objects.filter(specialization=pk)
	return render(request, 'service/specialization.html', {'specialization': specialization, 'disciplines': disciplines,  'spec_id': pk})

def discipline(request, pk):
	result = Discipline.objects.filter(specialization=pk)
	context = {'discipline': result}

	if request.method == "POST":
		form = ChooseDisciplineForm(request.POST)
		context['form'] = form
		if form.is_valid():
			return redirect('home')

	return render(request, 'service/discipline.html', context)

def vote(request, pk, specialization, faculty, teacher, student):
	discipline = Discipline.objects.get(id=pk)
	spec = Specialization.objects.get(id=specialization)
	faculty = Faculty.objects.get(id=faculty)
	_teacher = Profile.objects.get(id=teacher)
	_student = Profile.objects.get(id=student)

	result = Result.objects.create(
			discipline=discipline, 
			spec=spec,
			faculty=faculty,
			teacher=_teacher,
			student=_student,

		)

	return redirect('home')

@login_required
def cabinet(request):
	user_id = int(request.user.id)-1
	choosen_disciplines = Result.objects.filter(student=user_id)
	return render(request, 'service/cabinet.html', {'choosen_disciplines': choosen_disciplines})

def remove(request, pk):
	obj = Result.objects.get(pk=pk)
	obj.delete()
	return redirect('cabinet')