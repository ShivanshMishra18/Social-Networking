from django.db import models
from django.urls import reverse

class Profile(models.Model):
	Name = models.CharField(max_length=30)
	Email = models.EmailField(max_length=30)
	Username = models.CharField(max_length=20, unique=True)
	Birth_Date = models.DateField()

	def get_absolute_url(self):
		return reverse('website:details', kwargs={'pk':self.pk})

	def __str__(self):
		return self.Name + '-' + self.Username
			

class Post_Feed(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	Heading = models.CharField(max_length=30, null=True, blank=True)
	Descr = models.TextField(max_length=300)
	File_Link = models.FileField(null=True, blank=True)

	def __str__(self):
		return self.profile + '-' + self.Heading