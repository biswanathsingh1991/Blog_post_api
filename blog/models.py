from django.db import models
from django.urls import reverse
from core.models import UserProfile
# Create your models here.


class Blog(models.Model):
    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=True, null=True)
    containt = models.CharField(max_length=99999999, blank=True, null=True)
    image = models.ImageField(
        upload_to='blog/%Y/%m/%d/', blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:home')


class BlogComment(models.Model):
    blog_comment = models.CharField(max_length=999999, blank=True, null=True)
    blog = models.ManyToManyField(Blog)
    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="profile")
    # creade = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_comment


class Like(models.Model):
    blog_comment = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    userprofile = models.OneToOneField(
        UserProfile, on_delete=models.CASCADE, related_name="Blog_like")
    # creade = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
