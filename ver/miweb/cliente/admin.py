from django.contrib import admin

# Register your models here.
from cliente.models import Nombre
from cliente.models import Apellido
from cliente.models import Direccion

admin.site.register(Nombre)

admin.site.register(Apellido)

admin.site.register(Direccion)
