from asignaciones.models import Assignment, ProjectRol, Activity, TrackingHours
from django.contrib import admin
 

admin.site.register(Assignment)
admin.site.register(ProjectRol)
admin.site.register(Activity)
admin.site.register(TrackingHours)


class AssignmentAdmin(admin.options.ModelAdmin):
    list_display=('person' ,'rol', 'project', 'begin_date', 'end_date', 'status')
    list_filter=('project', 'rol', 'status')


class TrackingHoursAdmin(admin.options.ModelAdmin):
    list_display=('assigned_person' ,'end_date', 'activities')
    list_filter=('assigned_person')