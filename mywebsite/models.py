from django.db import models

# Create your models here.
from django.utils import timezone
# Create your models here.
from django.urls import reverse


class Projects(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
