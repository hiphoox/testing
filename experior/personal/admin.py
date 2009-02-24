from personal.models import Person, Region, Puesto
from django.contrib import admin


admin.site.register(Region)


admin.site.register(Puesto)



class PersonAdmin(admin.options.ModelAdmin):
    fieldsets =  [
        (None,              {'fields': ['first_name', 'last_name']}),
        ('Status',          {'fields': ['puesto', 'type', 'status', 'region']}),
        ('Contratacion',    {'fields': ['hiring_date','fire_date']}),
        ('Contacto',        {'fields': ['telephone_home', 'telephone_personal', 'email_1', 'email_2', 'prefered_email'] , 'classes': ['collapse']}),
        ('Otros',           {'fields': ['birthday','passport','visa'], 'classes': ['collapse']}),
        ('Comentarios',     {'fields': ['coment'], 'classes': ['collapse']}),
    ]
    list_display=('first_name' , 'last_name', 'status','region', 'puesto', 'antiguedad')
    list_filter=('status', 'region', 'puesto')

#class RegionAdmin(admin.options.ModelAdmin):
#    list_display=('name')
#    list_filter=('name')


admin.site.register(Person, PersonAdmin)

