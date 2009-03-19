from django.db import models

class businessPlan(models.Model):
    clave = models.CharField(max_lenght=20, blank='true')
    project = models.ForeignKey('Clientes.Project')
    concept = models.ForeignKey(concept , rel_class=ManyToMany)
    def __unicode__(self):
        return self.clave

class concept(models.Model):
    concept = models.CharField(max_lenght=100)
    monto = models.FloatField()
    def __unicode__(self):
        return self.concept

class operativeCommitment(models.Model):
    commitment =  models.ForeignKey(compromiso, rel_class=ManyToMany)
    def __unicode__(self):
        return self.commitment
    
class commitment(models.Model):
    stage = models.ForeignKey('planeacion.Stages')
    milestone = models.CharField(max_lenght=50)
    def __unicode__(self):
        return '%s' % (self.stage)
    