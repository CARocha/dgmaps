from django.contrib import admin
from lugares.models import *

class LugarAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lugar, LugarAdmin)