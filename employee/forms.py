from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from multiselectfield import MultiSelectField

from .models import Employee, Department, Position



class ChangeEmployeeDataForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('username', 'last_name', 'department', 'position', 'photo')



class EmployeeCreateForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'patronymic', 'department', 'position', 'photo')
        labels = {'department': 'Отдел', 'position': 'Должность', 'photo': 'Фото'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position'].queryset = Position.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['position'].queryset = Position.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['position'].queryset = self.instance.department.position_set.order_by('name')
