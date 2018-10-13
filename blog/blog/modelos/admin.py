from django.contrib import admin
from .models import Post
# Register your models here.
class ProjectAdmin(admin.ModelAdmin): # esta clase sirve para mostrar los modelos ocultos en este caso las fechas
    readonly_fields = ('created','updated') # se llama al nombre de la fecha creacion y actualizacion del modelo
admin.site.register(Post,ProjectAdmin) #para registrar mi modelo y se llama a la clase