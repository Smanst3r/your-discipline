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
	disciplines = Discipline.objects.filter(specialization=pk)
	result_by_student = Result.objects.filter(student=request.user.id-1)
	result = Result.objects.filter(spec=pk)

	disciplines_count_for_logged = result_by_student

	context = { 
			'disciplines': disciplines, 
			'disciplines_count': disciplines_count_for_logged, 
			'result': result }

	if request.method == "POST":
		form = ChooseDisciplineForm(request.POST)
		context['form'] = form
		if form.is_valid():
			return redirect('home')

	return render(request, 'service/discipline.html', context)

def discipline_detail(request, pk):
	discipline = Discipline.objects.get(id=pk)
	vote_counts = Result.objects.filter(discipline=discipline)
	return render(request, 'service/discipline_detail.html', {'discipline': discipline, 'vote_counts': vote_counts})

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