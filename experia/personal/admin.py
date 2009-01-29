from personal.models import Person, Region, Puesto
from django.contrib import admin
 

class PersonAdmin(admin.options.ModelAdmin):
    fieldsets =  [
        (None,              {'fields': ['first_name', 'last_name']}),
        ('Puesto',          {'fields': ['hiring_date', 'puesto']}),
        ('Region/Status',   {'fields': ['status', 'region',]}),
        ('Contacto',        {'fields': ['telephone_home', 'telephone_personal', 'email_1', 'email_2', 'prefered_email']}),
        ('Otros',           {'fields': ['passport']}),
    ]
    list_display=('first_name', 'status', 'puesto', 'antiguedad')
    list_filter=('first_name', 'status', 'region', 'puesto')

#class RegionAdmin(admin.options.ModelAdmin):
#    list_display=('name')
#    list_filter=('name')




admin.site.register(Person, PersonAdmin)

admin.site.register(Region)

admin.site.register(Puesto)








