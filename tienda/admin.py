from django.contrib import admin

# Register your models here.
from tienda.models import CategoriaProd, Producto

# se crea clase para filtrar los campos que queremos en el panel de administracion, en este caso ponemos
# created y updated que solo sean de lectura.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProd, CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)