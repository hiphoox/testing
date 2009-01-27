from django.db import models

# Create your models here.

class PersonStatus(models.Model):
    PERSON_STATUS_CHOICES=(('A','Activo'), ('I', 'Inactivo'))
    name = models.CharField(choices = PERSON_STATUS_CHOICES,  max_length=1)
    def __unicode__(self):
        return self.name

class PersonTypes(models.Model):
    PERSON_TYPES_CHOICES =(('I', 'Interno'), ('E', 'Externo'), ('S', 'Staff'))
    name = models.CharField(choices=PERSON_TYPES_CHOICES ,   max_length=1)
    def __unicode__(self):
        return self.name

class Regions(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Rols(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Puestos(models.Model):
    name = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.name

class Persons(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hiring_date = models.DateTimeField('date hired')
    region = models.ForeignKey(Regions)
    status = models.ForeignKey(PersonStatus)
    fire_date = models.DateTimeField('date fired',  blank='true')
    telephone_home = models.IntegerField('Telefono de casa', max_length=10)
    telephone_personal = models.IntegerField('Telefono celular', max_length=10)
    email_1 = models.CharField(max_length=40)
    email_2 = models.CharField(max_length=40)
    prefered_email = models.IntegerField()
    puesto = models.ForeignKey(Puestos,  related_name='interno')
    rol = models.ForeignKey(Rols,  related_name='externo')
    def __unicode__(self):
        return '%s %s' % (self.first_name ,  self.last_name)
