from django.contrib import admin

# Register your models here.
from servicios.models import Servicio

# se crea clase para filtrar los campos que queremos en el panel de administracion, en este caso ponemos
# created y updated que solo sean de lectura.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Servicio, ServicioAdmin)