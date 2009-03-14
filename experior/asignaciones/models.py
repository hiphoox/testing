from django.db import models

#class ProjectStatus(models.Model):
#    PROJECT_STATUS_CHOICES = (  ('PI','Por Iniciar')   ,   ('IN','Iniciado')    ,   ('EP','En Proceso') ,   ('CE','Cerrado')   , ('CA','Cancelado'))
#    name = models.CharField(max_length=2, choices=PROJECT_STATUS_CHOICES)
#    def __unicode__(self):
#        return self.name

class Rol(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Assignment(models.Model):
    PROJECT_STATUS_CHOICES = (  ('PI','Por Iniciar')   ,   ('IN','Iniciado')    ,   ('EP','En Proceso') ,   ('CE','Cerrado')   , ('CA','Cancelado'))
    person = models.ForeignKey('personal.Person')
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(choices=PROJECT_STATUS_CHOICES, max_length=2)
    project = models.ForeignKey('clientes.Project')
    rol = models.ForeignKey(Rol)
    def __unicode__(self):
        return '%s - %s' % (self.person ,  self.project)
 
class TrackingHours(models.Model):
    person = models.ForeignKey('personal.Person')
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def __unicode__(self):
        return '' % (self.name, )

class ReportActivity(models.Model):
    activity = models.ForeignKey(Activity)
    detail = models.CharField(max_length=40)
    time = models.IntegerField()
    def __unicode__(self):
        return self.stage

class Activity(models.Model):
    HOUR_TRACKING_STAGES = (('Analisis','Analisis')  ,   ('Diseno','Diseno')  ,   ('Ejecucion','Ejecucion') , ('Regresion','Regresion') , ('Estabilizacion','Estabilizacion') , ('Cierre','Cierre'))
    name = models.CharField(max_length=20)
    stage = models.CharField(choices=HOUR_TRACKING_STAGES , max_length=14)
    def __unicode__(self):
        return '%s - %s' % (stage, self.name)