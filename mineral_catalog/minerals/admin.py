from django.contrib import admin

# Register your models here.
from .models import Mineral


class MineralAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Mineral, MineralAdmin)
