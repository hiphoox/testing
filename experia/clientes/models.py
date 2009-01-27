from django.db import models

######
###Organizational
 
#done
class InternalBusinessArea(models.Model):
    name=models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
 
class OrganizationalPersonStatus(models.Model):
    CLIENT_STATUS = (('A', 'Activo' ,) , ('I', 'Inactivo'))
    name = models.CharField( choices=CLIENT_STATUS,  max_length=20) #active|inactive
    def __unicode__(self):
        return self.name
 
#done
class BusinesClasses(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
 
class Clients(models.Model):
    name = models.CharField(max_length=50)
    legal_ame = models.CharField(max_length=50)
    bussines_class = models.ForeignKey(BusinesClasses)
    def __unicode__(self):
        return self.name

class ClientBusiness(models.Model):
    client = models.ManyToManyField(Clients)
    b_class = models.ManyToManyField(BusinesClasses)
    i_class = models.ManyToManyField(InternalBusinessArea)
    def __unicode__(self):
        return '%s - %s > %s' % (Clients.name ,  BusinesClasses.name ,  InternalBusinessArea.name)
#
class OrganizationalPersons(models.Model):
    name = models.CharField(max_length=200)
    work_for = models.ForeignKey(Clients)
    status = models.ForeignKey(OrganizationalPersonStatus)
    email_1 = models.CharField(max_length=40)
    puesto = models.CharField(max_length=40)
    intern_area = models.ForeignKey(InternalBusinessArea)
    def __unicode__(self):
        return self.name

class ApplicationModules(models.Model):
    name=models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Applications(models.Model):
    full_name= models.CharField(max_length=200)
    short_name = models.CharField(max_length=15)
    module = models.ManyToManyField(ApplicationModules)
    def __unicode__(self):
        return self.short_name

class Projects(models.Model):
    name = models.CharField(max_length=100)
    client = models.ForeignKey(Clients)
    app = models.ManyToManyField(Applications)
    def __unicode__(self):
        return self.name
    
    
    
    
    
    
    
    
