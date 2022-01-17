from django.contrib import admin

# Register your models here.
from .models import Position


class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Position, PositionAdmin)



