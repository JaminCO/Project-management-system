from django.db import models
from django.contrib.auth.models import User
# from profiles.models import Profile as profile


# Create your models here.
class Projects(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	# user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	# task = models.ManyToManyField(Task, blank=True, related_name='tasks')
	starting = models.DateField()
	deadline = models.DateField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	description = models.TextField(default="no description...", blank=True)
	complete = models.BooleanField(default=False)
	

	def __str__(self):
			return f"{self.name}"
	
	class Meta:
			ordering = ['complete']

class Task(models.Model):
	project = models.ForeignKey(Projects, on_delete=models.CASCADE)
	taskname = models.CharField(max_length=100)
	starting = models.DateField()
	deadline = models.DateField()
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	description = models.TextField(default="no description...", null=True, blank=True)
	
	def __str__(self):
			return str(self.taskname)

	class Meta:
			ordering = ['complete']