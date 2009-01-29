from django.db import models

import datetime
# Create your models here.

class PersonStatus(models.Model):
    PERSON_STATUS_CHOICES=(('A','Activo'), ('I', 'Inactivo'))
    name = models.CharField(choices = PERSON_STATUS_CHOICES,  max_length=1)
    def __unicode__(self):
        return self.name

class PersonType(models.Model):
    PERSON_TYPES_CHOICES =(('I', 'Interno'), ('E', 'Externo'), ('S', 'Staff'))
    name = models.CharField(choices=PERSON_TYPES_CHOICES ,   max_length=1)
    def __unicode__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Puesto(models.Model):
    name = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.name

class Person(models.Model):
    PREFERED_MAIL_CHOICE = (('1','email 1'),('2','email 2'))
    PERSON_STATUS_CHOICES=(('A','Activo'), ('I','Inactivo'))
    PERSON_TYPES_CHOICES =(('I','Interno'), ('E','Externo'), ('S','Staff'))
    first_name = models.CharField( 'Nombres', max_length=30)
    last_name = models.CharField( 'Apellidos', max_length=30)
    hiring_date = models.DateField('date hired')
    birthday = models.DateField('Cumpleanos', null=True,blank=True)
    region = models.ForeignKey(Region)
    status = models.CharField(choices=PERSON_STATUS_CHOICES, max_length=7)
    type = models.CharField(choices=PERSON_TYPES_CHOICES, max_length=7)
    fire_date = models.DateField('date fired', blank=True)
    telephone_home = models.IntegerField('Telefono de casa', max_length=10, blank=True)
    telephone_personal = models.IntegerField('Telefono celular', max_length=10, blank=True)
    email_1 = models.CharField(max_length=40, blank=True)
    email_2 = models.CharField(max_length=40, blank=True)
    prefered_email = models.CharField(choices=PREFERED_MAIL_CHOICE, blank='true', max_length=1)
    puesto = models.ForeignKey(Puesto,  related_name='interno', blank=True)
    passport = models.CharField(max_length=20, blank=True)
    visa = models.CharField(max_length=20, blank = True)
    coment = models.CharField('Comentario', max_length=100, blank=True)
    def __unicode__(self):
        return '%s %s' % (self.first_name ,  self.last_name)
    def antiguedad(self):
        return self.hiring_date - datetime.date.today()
