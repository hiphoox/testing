from django.db import models

#done
class Audits(models.Model):
    person = models.ForeignKey('personal.Persons')
    project = models.ForeignKey('clientes.Projects')
    start_date = models.DateTimeField('start')
    interview_date = models.DateTimeField()
    end_date = models.DateTimeField('end')
    fase_analisis = models.IntegerField('Analisis')
    fase_diseno = models.IntegerField('Diseno')
    fase_ejecucion = models.IntegerField('Ejecucion')
    fase_regresion = models.IntegerField('Regresion')
    fase_estabilizacion = models.IntegerField('Estabilizacion')
    fase_cierre = models.IntegerField('Cierre')
    other_commens = models.CharField(max_length=500)
    def __unicode__(self):
        return '%s - %s (%s)' % (self.person ,  self.project ,  self.end_date)

class Coaching(models.Model):
    person = models.ForeignKey('personal.Persons')
    project = models.ForeignKey('clientes.Projects')
    session_date = models.DateTimeField('Session')
    fase_analisis = models.IntegerField('Analisis')
    fase_diseno = models.IntegerField('Diseno')
    fase_ejecucion = models.IntegerField('Ejecucion')
    fase_regresion = models.IntegerField('Regresion')
    fase_estabilizacion = models.IntegerField('Estabilizacion')
    fase_cierre = models.IntegerField('Cierre')
    other_commens = models.CharField(max_length=500)
    def __unicode__(self):
        return '%s - %s (%s)' % (self.person ,  self.project ,  self.session_date)






