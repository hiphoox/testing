from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=200)
    module = models.ForeignKey(Module)
    duration = models.IntegerField('Duracion')
    def __unicode__(self):
        return self.name

class CourseStatus(models.Model):
    COURSE_STATUS_CHOICE = (('E', 'En Proceso') ,   ('P','Planeado')    ,   ('C','Cancelado')   , ('F','Finalizado') )
    name = models.CharField(max_length=1, choices=COURSE_STATUS_CHOICE)
    def __unicode__(self):
        return self.name

class CourseControl(models.Model):
    course = models.ForeignKey(Course)
    person = models.ManyToManyRel('personal.Person')
    begin_date = models.DateTimeField('start')
    end_date = models.DateTimeField('end')
    grade = models.IntegerField(blank='true')
    duration = models.IntegerField(blank='true')
    status = models.ForeignKey(CourseStatus)
    def __unicode__(self):
        return "%s : %s : %s %s %s" & (self.person , self.course, self.grade, self.status, self.begin_date )

class Topic(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class KnowledgeMatrix(models.Model):
    person = models.ManyToManyField('personal.Person')
    topics = models.ManyToManyField(Topic)
    coment = models.CharField(max_length=200)
    def __unicode__(self):
        return self.person