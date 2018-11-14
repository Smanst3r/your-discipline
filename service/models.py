from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
	is_teacher = models.BooleanField("teacher status", default=False)
	is_student = models.BooleanField("student status", default=False)
	faculty = models.ForeignKey('service.Faculty', on_delete=models.CASCADE)
	specialization = models.ForeignKey('service.Specialization', on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username

class Faculty(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Specialization(models.Model):
	name = models.CharField(max_length=200)
	faculty = models.ForeignKey('service.Faculty', on_delete=models.CASCADE, related_name="specs")

	def __str__(self):
		return "{}, ({})".format(self.name, self.faculty)

class Discipline(models.Model):
	faculty = models.ForeignKey('service.Faculty', on_delete=models.CASCADE)
	specialization = models.ForeignKey('service.Specialization', related_name="disciplines")
	name = models.CharField(max_length=200)
	teacher = models.ForeignKey('service.Profile', on_delete=models.CASCADE)
	about = models.TextField(max_length=500, default="Опис дисципліни. Наприклад Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. ")

	def __str__(self):
		return "{}, ({})".format(self.name, self.faculty)

class Result(models.Model):
	student = models.ForeignKey('service.Profile', related_name="student")
	teacher = models.ForeignKey('service.Profile', related_name="teacher")
	faculty = models.ForeignKey('service.Faculty')
	spec = models.ForeignKey('service.Specialization')
	discipline = models.ForeignKey('service.Discipline')

	def __str__(self):
		return "{} - вибрав: {}".format(self.student, self.discipline)
