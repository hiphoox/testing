from django.db import models

######
###Organizational
 
#done

## directly addeded to project as choice
#class ProjectType(models.Model):
#    PROJECT_TYPE_CHOICES = (('Fabrica','Fabrica'),('Asignacion','Asignacion'))
#    name=models.CharField(max_length=10, choices=PROJECT_TYPE_CHOICES)
#    def __unicode__(self):
#        return self.name

## directly addeded to project as choice
#class ProjectComercialType(models.Model):
#    PROJECT_COMERCIAL_TYPE_CHOICES = (('C','Cerrado'),('T','Tiempo y Materiales'))
#    name=models.CharField(max_length=1, choices=PROJECT_COMERCIAL_TYPE_CHOICES)
#    def __unicode__(self):
#        return self.name

class InternalBusinessArea(models.Model):
    name=models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

## directly addeded to organizationalperson as choice
#class OrganizationalPersonStatus(models.Model):
#    CLIENT_STATUS = (('A', 'Activo' ,) , ('I', 'Inactivo'))
#    name = models.CharField( choices=CLIENT_STATUS,  max_length=20) #active|inactive
#    def __unicode__(self):
#        return self.name
 

class BusinesClass(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
 
class Client(models.Model):
    name = models.CharField(max_length=50)
    legal_ame = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class ClientBusiness(models.Model):
    client = models.ManyToManyField(Client)
    b_class = models.ManyToManyField(BusinesClass)
    i_class = models.ManyToManyField(InternalBusinessArea)
    def __unicode__(self):
        return '%s - %s > %s' % (Clients.name ,  BusinesClasses.name ,  InternalBusinessArea.name)

class OrganizationalPerson(models.Model):
    CLIENT_STATUS = (('Activo', 'Activo' ,) , ('Inactivo', 'Inactivo'))
    name = models.CharField(max_length=200)
    work_for = models.ForeignKey(Client)
    status = models.CharField(choices=CLIENT_STATUS, max_length=8)
    email_1 = models.CharField(max_length=40)
    puesto = models.CharField(max_length=40)
    intern_area = models.ForeignKey(InternalBusinessArea)
    def __unicode__(self):
        return '%s from %s' % ( Clients.name, self.name)

class ApplicationModule(models.Model):
    name=models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Application(models.Model):
    full_name= models.CharField(max_length=200)
    short_name = models.CharField(max_length=15)
    module = models.ManyToManyField(ApplicationModule)
    def __unicode__(self):
        return self.short_name

class Project(models.Model):
    PROJECT_TYPE_CHOICES = (('Fabrica','Fabrica'),('Asignacion','Asignacion'))
    PROJECT_COMERCIAL_TYPE_CHOICES = (('Cerrado','Cerrado'),('Tiempo y Materiales','Tiempo y Materiales'))
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Client)
    app = models.ManyToManyField(Application)
    type = models.CharField(choices=PROJECT_TYPE_CHOICES, blank ='true', max_length=19)
    comtype = models.CharField(choices=PROJECT_COMERCIAL_TYPE_CHOICES, blank='true', max_length=10, short_name='Contract Type')
    def __unicode__(self):
        return self.name
    
#class ProjectApps(models.Model):
#    project = models.ManyToManyField(Project)
#    app = models.ManyToManyRel(Application)

    
    
    
    
    
    
    
