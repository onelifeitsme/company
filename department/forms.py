from department.models import Department
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from employee.models import Employee
from multiselectfield import MultiSelectField



class CreateDepartmentForm(ModelForm):
    emps = Employee.objects.all()
    emp_choices = [(emp, emp) for emp in emps]
    transfer_employee_choise = forms.MultipleChoiceField(
    required=False,
    widget=forms.CheckboxSelectMultiple,
    choices=emp_choices,
    label='Сотрудники в новый отдел')

    class Meta:
       model = Department
       fields = ['name', 'transfer_employee_choise']