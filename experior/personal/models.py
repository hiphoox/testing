from django.db import models

import datetime
# Create your models here.

#class PersonStatus(models.Model):
#    PERSON_STATUS_CHOICES=(('A','Activo'), ('I', 'Inactivo'))
#    name = models.CharField(choices = PERSON_STATUS_CHOICES,  max_length=1)
#    def __unicode__(self):
#        return self.name
#
#class PersonType(models.Model):
#    PERSON_TYPES_CHOICES =(('I', 'Interno'), ('E', 'Externo'), ('S', 'Staff'))
#    type = models.CharField(choices=PERSON_TYPES_CHOICES ,   max_length=1)
#    def __unicode__(self):
#        return self.type

class Region(models.Model):
    region = models.CharField(max_length=20)
    def __unicode__(self):
        return self.region

class Puesto(models.Model):
    name = models.CharField(max_length = 50)
    acronim = models.CharField(max_length = 5)
    def __unicode__(self):
        return self.acronim

class Person(models.Model):
    PREFERED_MAIL_CHOICE = (('email 1','email 1'),('email 2','email 2'))
    PERSON_STATUS_CHOICES=(('Activo','Activo'), ('Inactivo','Inactivo'))
    PERSON_TYPES_CHOICES =(('Interno','Interno'), ('Externo','Externo'), ('Staff','Staff'))
    first_name = models.CharField( 'Nombres', max_length=30)
    last_name = models.CharField( 'Apellidos', max_length=30)
    hiring_date = models.DateField('date hired')
    birthday = models.DateField('Cumpleanos', null=True, blank=True)
    region = models.ForeignKey(Region)
    status = models.CharField(choices=PERSON_STATUS_CHOICES, max_length=7)
    type = models.CharField(choices=PERSON_TYPES_CHOICES, max_length=7)
    fire_date = models.DateField('date fired',null=True, blank=True)
    telephone_home = models.IntegerField('Telefono de casa', max_length=10, null=True,blank=True)
    telephone_personal = models.IntegerField('Telefono celular', max_length=10, null=True,blank=True)
    email_1 = models.EmailField(blank=True)
    email_2 = models.EmailField(blank=True)
    prefered_email = models.CharField(choices=PREFERED_MAIL_CHOICE, blank='true', max_length=7)
    puesto = models.ForeignKey(Puesto, related_name='interno', blank=True)
    passport = models.CharField(max_length=20, blank=True)
    visa = models.CharField(max_length=20, blank = True)
    coment = models.CharField('Comentario', max_length=100, blank=True)
    nomina = models.IntegerField('Nomina', max_length=6, null=True, blank=True)
    def __unicode__(self):
        return '%s %s' % (self.first_name ,  self.last_name)
    def antiguedad(self):
        return datetime.date.today() - self.hiring_date
