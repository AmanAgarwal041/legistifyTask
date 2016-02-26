from django.db import models

# Create your models here.

class UserDetail(models.Model):
    uid = models.CharField(max_length=120, blank=False, unique=True)
    pno = models.IntegerField(max_length=12, blank=False)
    age = models.IntegerField(max_length=3, blank=False)
    gen = models.CharField(max_length=1, blank=False)

    def __unicode__(self):
        return self.uid

class LawyerDetail(models.Model):
    lid = models.CharField(max_length=120, blank=False, unique=True)
    pno = models.IntegerField(max_length=12, blank=False)
    speciality = models.CharField(max_length=120, blank=False)
    age = models.IntegerField(max_length=3, blank=False)
    experience = models.IntegerField(max_length=2, blank=False)
    gen = models.CharField(max_length=1, blank=False)

    def __unicode__(self):
        return self.lid
