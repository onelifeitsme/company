from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    # list_display = ('username', 'last_name', 'department', 'position', 'slug', 'photo')
    prepopulated_fields = {'slug': ('username', 'last_name',)}



admin.site.register(Employee, EmployeeAdmin)

from django.contrib import admin

# Register your models here.
