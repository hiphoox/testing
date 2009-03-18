from django.db import models

#class ProjectStatus(models.Model):
#    PROJECT_STATUS_CHOICES = (  ('PI','Por Iniciar')   ,   ('IN','Iniciado')    ,   ('EP','En Proceso') ,   ('CE','Cerrado')   , ('CA','Cancelado'))
#    name = models.CharField(max_length=2, choices=PROJECT_STATUS_CHOICES)
#    def __unicode__(self):
#        return self.name

class ProjectRol(models.Model):
    name = models.CharField(max_length=50)
    acronim = models.CharField(max_length=5)
    def __unicode__(self):
        return self.acronim

class Assignment(models.Model):
    PROJECT_STATUS_CHOICES = (  ('PI','Por Iniciar')   ,   ('IN','Iniciado')    ,   ('EP','En Proceso') ,   ('CE','Cerrado')   , ('CA','Cancelado'))
    person = models.ForeignKey('personal.Person')
    begin_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=PROJECT_STATUS_CHOICES, max_length=2)
    project = models.ForeignKey('clientes.Project')
    rol = models.ForeignKey(ProjectRol)
    time = models.IntegerField(help_text='Tiempo de la asignacion en horas')
    def __unicode__(self):
        return '%s - %s' % (self.project, self.person)

class Activity(models.Model):
    HOUR_TRACKING_STAGES = (('Analisis','Analisis')  ,   ('Diseno','Diseno')  ,   ('Ejecucion','Ejecucion') , ('Regresion','Regresion') , ('Estabilizacion','Estabilizacion') , ('Cierre','Cierre'))
    name = models.CharField(max_length=80)
    stage = models.CharField(choices=HOUR_TRACKING_STAGES , max_length=14)
    billable = models.BooleanField()
    def __unicode__(self):
        return '%s - %s' % (self.stage, self.name)

class ReportedActivity(models.Model):
    activity = models.ForeignKey(Activity)
    detail = models.CharField(max_length=40, blank='true')
    time = models.IntegerField(help_text='Time in integer hours')
    def __unicode__(self):
        return '%s : %ihrs' % (self.activity, self.time)

class TrackingHours(models.Model):
    assignment = models.ForeignKey(Assignment)
    begin_date = models.DateField()
    end_date = models.DateField()
    activities = models.ManyToManyField(ReportedActivity)
    def __unicode__(self):
        return '%s - %s' % (self.assignment, self.end_date)