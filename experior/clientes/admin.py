from clientes.models import Client, Project, Application, ApplicationModule
from django.contrib import admin

admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Application)
#admin.site.register(ProjectType)
admin.site.register(ApplicationModule)