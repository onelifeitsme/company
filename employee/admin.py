from django.contrib import admin

# Register your models here.
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('username', 'last_name',)}


admin.site.register(Employee, EmployeeAdmin)
