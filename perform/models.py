from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)


	def __str__(self):
		return self.firstname+ " " +self.lastname


class Parameter(models.Model):
	paraname = models.CharField(max_length=30)
	
	def __str__(self):
		return self.paraname

class Employee_Para(models.Model):
	employee = models.ForeignKey(Employee)
	parameter = models.ForeignKey(Parameter)
	weightage = models.PositiveIntegerField(default=0)
	score    =  models.PositiveIntegerField()
	pub_month = models.CharField(max_length=7)

 #class Whole_thing(models.Model):


	#def save(self):
	#	year = int(self.pub_month[:-4])
	#	month = int(self.pub_month[2:])
	#	if month<1 or month>12:
	#		raise ValueError
	#	if year<2000 or year>2020:
	#		raise ValueError
	#		self.save()
         

	#def __str__(self):
	#	return employee+ " " +parameter





	
		





# Create your models here
