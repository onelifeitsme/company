from django.contrib import admin

# Register your models here.
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ['name']}


admin.site.register(Department, DepartmentAdmin)
