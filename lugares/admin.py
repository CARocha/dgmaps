from django.contrib import admin
from lugares.models import *

class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre1', 'descripcion',)


admin.site.register(Lugar, LugarAdmin)