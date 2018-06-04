from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    containt = models.CharField(max_length=99999999, blank=True, null=True)
    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:home')
