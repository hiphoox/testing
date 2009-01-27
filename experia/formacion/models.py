from django.db import models

class Modules(models.Model):
    name = models.CharField(max_length=10)
    tags = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=200)
    module = models.ForeignKey(Modules)
    duration = models.IntegerField()
    def __unicode__(self):
        return self.name

class CourseControls(models.Model):
    course = models.ForeignKey(Courses)
    person = models.ManyToManyField('personal.Persons')
    begin_date = models.DateTimeField('start')
    end_date = models.DateTimeField('end')
    grade = models.IntegerField()
    duration = models.IntegerField()

class Topics(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name

class KnowledgeMatrix(models.Model):
    person = models.ManyToManyField('personal.Persons')
    topics = models.ManyToManyField(Topics)
