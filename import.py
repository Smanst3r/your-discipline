import csv, sys, os

project_dir = "/home/paul/python/choose-discipline/mysite/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from service.models import Specialization, Faculty, Discipline, Profile

data = csv.reader(open("/home/paul/python/choose-discipline/disciplines.csv"), delimiter=",")

for row in data:
	if row[0] != "name" and row[1] != "faculty":
		discipline = Discipline()
		discipline.faculty = Faculty(id=row[0])
		discipline.specialization = Specialization(id=row[1])
		discipline.name = row[2]
		discipline.teacher = Profile(id=row[3])
		discipline.save()
