from django.db import models
from django.utils.text import slugify
# Create your models here.

class Artikel(models.Model):
	judul		= models.CharField(max_length=50)
	slug 		= models.SlugField(blank=True, unique=True, editable=False)
	penulis 	= models.CharField(max_length=20)
	isi 		= models.TextField()
	kategori 	= models.CharField(max_length=225)
	published	= models.DateTimeField(auto_now_add=True)
	updated     = models.DateTimeField(auto_now=True)

	def save(self):
		self.slug = slugify(self.judul)
		super().save()

	def get_absolute_url(self):
		return '{slug}/'.format(slug=self.slug)


	def __str__(self):
		return self.judul