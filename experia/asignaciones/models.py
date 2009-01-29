from django.db import models

class ProjectStatus(models.Model):
    PROJECT_STATUS_CHOICES = (  ('PI','Por Iniciar')   ,   ('IN','Iniciado')    ,   ('EP','En Proceso') ,   ('CE','Cerrado')   , ('CA','Cancelado'))
    name = models.CharField(max_length=2, choices=PROJECT_STATUS_CHOICES)
    def __unicode__(self):
        return self.name

class Rol(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Assignment(models.Model):
    person = models.ForeignKey('personal.Person')
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.ForeignKey(ProjectStatus)
    project = models.ForeignKey('clientes.Project')
    rol = models.ForeignKey(Rol)
    def __unicode__(self):
        return '%s - %s' % (self.person ,  self.project)
 