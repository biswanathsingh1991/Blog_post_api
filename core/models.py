from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name=None, name=None, auto_now=True, auto_now_add=False)
    # modified = models.DateTimeField(verbose_name=None, name=None, auto_now=True, auto_now_add=True)
    profile_pic = models.ImageField(verbose_name=None, name=None,
                                    width_field=None, height_field=None, upload_to="profile_pic/%Y/%m/%d/")
    mobile_no = models.IntegerField(verbose_name=None, name=None, primary_key=False, max_length=None, unique=False, blank=False, null=False,
                                    db_index=False, rel=None, default=0, editable=True,
                                    serialize=True, unique_for_date=None, unique_for_month=None, unique_for_year=None, choices=None,
                                    help_text='', db_column=None, db_tablespace=None, auto_created=False, validators=(), error_messages=None)
    country = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    zipcode = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.user)


@ receiver(post_save, sender=User)
def uerprofilecreat(sender, **kwargs):
    if kwargs.get('created'):
        UserProfile.objects.get_or_create(User=kwargs.get('instance'))
