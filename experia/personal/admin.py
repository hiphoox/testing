from personal.models import Persons
from django.contrib import admin
 
admin.site.register(Persons)

class PersonsAdmin(admin.options.ModelAdmin):
    admin.options.ModelAdmin.list_display=('first_name', 'status', 'rol')
    admin.options.ModelAdmin.list_filter=('first_name', 'status', 'region', 'puesto')















