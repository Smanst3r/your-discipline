from django import forms
from django.contrib.auth.models import User
from .models import Profile, Faculty, Specialization, Discipline



class FacultyForm(forms.ModelForm):
	
	class Meta:
		model = Faculty
		fields = ('name',)

class SpecializationForm(forms.ModelForm):

	class Meta:
		model = Specialization
		fields = ('faculty', 'name')

class ChooseDisciplineForm(forms.ModelForm):

	class Meta:
		model = Discipline
		fields = ('name',)