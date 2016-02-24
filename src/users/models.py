from django.db import models

# Create your models here.

class Login(models.Model):
    uname = models.EmailField(max_length=120,blank=False)
    pword = models.CharField(max_length=120,blank=False)
    utype = models.IntegerField(blank=False)

    def __unicode__(self):
        return self.uname
