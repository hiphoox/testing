from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    module = models.ForeignKey(Module)
    duration = models.IntegerField('Duracion', blank=True, null=True)
    tags = models.CharField(max_length=50, blank=True)
    def __unicode__(self):
        return "%s : %s" % (self.module, self.name)

class CourseControl(models.Model):
    COURSE_STATUS_CHOICE = (('E', 'En Proceso') ,   ('P','Planeado')    ,   ('C','Cancelado')   , ('F','Finalizado') )
    person = models.ForeignKey('personal.Person')
    course = models.ForeignKey(Course)
    begin_date = models.DateField('start')
    end_date = models.DateField('end', null='true')
    grade = models.IntegerField(null='true', blank='true')
    duration = models.IntegerField(blank='true', null='true')
    status = models.CharField(choices=COURSE_STATUS_CHOICE , max_length=1)
    def __unicode__(self):
        return "%s : %s : %s %s %s" & (self.person , self.course, self.grade, self.status, self.begin_date )

class Topic(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class KnowledgeMatrix(models.Model):
    person = models.ManyToManyField('personal.Person')
    topics = models.ManyToManyField(Topic)
    coment = models.CharField(max_length=200, blank=True)
    def __unicode__(self):
        return "%s - %s : %s" % (self.person, self.topics, self.coment)