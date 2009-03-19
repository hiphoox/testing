from django.db import models

class concept(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class businessPlan(models.Model):
    clave = models.CharField(max_length=20)
    project = models.ForeignKey('clientes.Project')
    concept = models.ForeignKey(concept)
    amount = models.FloatField()
    def __unicode__(self):
        return self.clave



class Stages(models.Model):
    STAGES = (('A','Analisis')  ,   ('D','Diseno')  ,   ('E','Ejecucion')   ,   ('R','Regresion') ,   ('C','Cierre'))
    name = models.CharField(max_length=10, choices=STAGES)
    def __unicode__(self):
        return self.name


class operativeCommitment(models.Model):
    project = models.ForeignKey('clientes.Project')
    stage = models.ForeignKey(Stages)
    milestone = models.CharField(max_length=30)
    date = models.DateField(blank=True, null=True)
    def __unicode__(self):
        return self.project