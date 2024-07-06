from django.db import models
from django.urls import reverse

class Authors(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    birthdate = models.DateField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'slug': self.slug})

class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    published_date = models.DateField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books-detail', kwargs={'slug': self.slug})
