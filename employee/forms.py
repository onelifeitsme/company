from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Employee, Position



class EmployeeCreateForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'patronymic', 'department', 'position', 'photo', 'is_staff')
        labels = {'username': 'Логин для входа', 'department': 'Отдел', 'position': 'Должность', 'photo': 'Фото', 'is_staff': 'Сделать администратором'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['position'].queryset = Position.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['position'].queryset = Position.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['position'].queryset = self.instance.department.position_set.order_by('name')



class ChangeEmployeeDataForm(ModelForm):
    class Meta:
        model = Employee
        fields = ('username', 'last_name', 'department', 'position', 'photo')