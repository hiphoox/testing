from django.contrib import admin
from formacion.models import Module, Course, CourseControl, Topic, KnowledgeMatrix

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(CourseControl)

class CourseControlAdmin(admin.options.ModelAdmin):
    list_display=('person' , 'course', 'status', 'grade')
    list_filter=('status', 'course')

class CourseAdmin(admin.options.ModelAdmin):
    list_display=('name', 'module')
    list_filter=('module')

#admin.site.register(Topic, KnowledgeMatrix)
#
#admin.site.register(Module, Course)
#admin.site.register(CourseControl)
#admin.site.register(Topic, KnowledgeMatrix)

#class CouseControlAdmin(admin.options.ModelAdmin):
#    admin.site.register(Module,Course,CourseControl)


#class PersonsAdmin(admin.options.ModelAdmin):
#    admin.options.ModelAdmin.list_display=('first_name', 'status', 'rol')
#    admin.options.ModelAdmin.list_filter=('first_name', 'status', 'region', 'puesto')















