from django.db import models


########
### Timeline

# Create your models here.
class PersonStatus(models.Model):
    PERSON_STATUS_CHOICES(('A','Activo'), ('I', 'Inactivo'))
    name = models.CharField(choices = PERSON_STATUS_CHOICES)
    def __unicode__(self):
        return self.name

class PersonTypes(models.Model):
    PERSON_TYPES_CHOICES =(('I', 'Interno'), ('E', 'Externo'), ('S', 'Staff'))
    name = models.CharField(choices=PERSON_TYPES_CHOICES)
    def __unicode__(self):
        return self.name

#done
class Regions(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

#done
class Rols(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Puestos(models.Model):
    name = nodels.CharField(max_lenght = 50)
    def __unicode__(self):
        return self.name

#done
class Persons(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    hiring_date = models.DateTimeField('date hired')
    region = models.ForeignKey(Regions)
    status = models.ForeignKey(PersonStatus)
    fire_date = models.DateTimeField('date fired')
    telephone_home = models.IntegerField('Telefono de casa', max_lenght=10)
    telephone_personal = models.IntegerField('Telefono celular', max_lenght=10)
    email_1 = models.CharField(max_length=40)
    email_2 = models.CharField(max_length=40)
    prefered_email = models.IntegerField()
    puesto = models.ForeignKey(Puestos,  related_name='interno')
    rol = models.ForeignKey(Rols,  related_name='externo')
    def __unicode__(self):
        return '%s %s' % (self.firstName ,  self.lastName)

########
### Career
#done
class Modules(models.Model):
    name = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

#done
class Courses(models.Model):
    name = models.CharField(max_length=200)
    module = models.ForeignKey(Modules)
    duration = models.IntegerField()
    def __unicode__(self):
        return self.name

#done
class CourseControls(models.Model):
    course = models.ForeignKey(Courses)
    person = models.ForeignKey(Persons)
    begin_date = models.DateTimeField('start')
    end_date = models.DateTimeField('end')
    grade = models.IntegerField()
    duration = models.IntegerField()

######
###Audit

#done
class Audits(models.Model):
    person = models.ForeignKey(Persons)
    start_date = models.DateTimeField('start')
    interview_date = models.DateTimeField()
    end_date = models.DateTimeField('end')
    fase_analisis = models.IntegerField('Analisis')
    fase_diseno = models.IntegerField()
    fase_ejecucion = models.IntegerField()
    fase_regresion = models.IntegerField()
    fase_estabilizacion = models.IntegerField()
    fase_cierre = models.IntegerField()
    other_commens = models.CharField(max_length=500)
    
######
###Organizational

#done
class InternalBusinessArea(models.Model):
    name=models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class OrganizationalPersonStatus(models.Model):
    name = models.CharField(max_length=20) #active|inactive
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

######
###ASSIGNMENT

#done
class ProjectPersonStatus(models.Model):
    name = models.CharField(max_length=40)
    def __unicode__(self):
        return self.name

#done
class ProjectStatus(models.Model):
    name = models.CharField(max_length=40)
    def __unicode__(self):
        return self.name

#done
class Technologies(models.Model):
    name = models.CharField(max_length=40)
    def __unicode__(self):
        return self.name

#done
class ApplicationNames(models.Model):
    name = models.CharField(max_length=40)
    def __unicode__(self):
        return self.name

class Projects(models.Model):
    name= models.CharField(max_length=100)
    technology = models.ForeignKey(Technologies)
    application_name = models.ForeignKey(ApplicationNames)
    business_area = models.ForeignKey(InternalBusinessArea)
    ocp_contact = models.ForeignKey(OrganizationalPersons,  related_name='ocp')
    comercial_contact = models.ForeignKey(OrganizationalPersons,  related_name='comercial')
    client_leader = models.ForeignKey(OrganizationalPersons,  related_name='leader')
    status = models.ForeignKey(ProjectStatus)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def __unicode__(self):
        return self.name

class Assignments(models.Model):
    person = models.ForeignKey(Persons)
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.ForeignKey(ProjectPersonStatus)
    project = models.ForeignKey(Projects)
    def __unicode__(self):
        return '%s - %s' % (Projects.name ,  Persons.first_name)
