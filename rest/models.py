from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

'''
def upload_location(instance, filename, **kwargs):
    file_path = f'blog/{instance.title}-{filename}'
    return file_path

this function to customize file path
'''


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def save(self):
        self.slug = slugify(self.author.username+'-'+self.title)
        super().save()

    def __str__(self):
        return f'{self.id}. {self.title} - {self.author.username}'
