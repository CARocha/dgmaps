from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Lugar(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    user = models.ForeignKey(User)

    def __unicode__(self):
    	return self.nombre

    def nombre1(self):
    	return u'%s' % self.nombre
    nombre1.allow_tags = True
