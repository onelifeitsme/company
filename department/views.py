from django.contrib.auth.mixins import LoginRequiredMixin
from position.models import Position
from .forms import CreateDepartmentForm
from django.http import HttpResponseRedirect
from employee.models import Employee
from .models import Department
from django.views.generic import FormView, ListView, DetailView, DeleteView
from django import forms


class DepartmentCreateView(LoginRequiredMixin, FormView):
    # ПРЕДСТАВЛЕНИЕ СОЗДАНИЯ ОТДЕЛА
    form_class = CreateDepartmentForm
    template_name = 'department/create_department.html'
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            depatment_name = form.cleaned_data['name']
            positions = request.POST.getlist('position')
            Department.objects.create(name=depatment_name)
            new_department = Department.objects.get(name=depatment_name)
            for position in positions:
                Position.objects.create(
                    name=position,
                    department=new_department,
                    vacant=True
                )
        return HttpResponseRedirect('departments')


class DepartmentDeleteView(DeleteView):
    # ППРЕДСТАВЛЕНИЕ УДАЛЕНИЯ ОТДЕЛА
    model = Department
    template_name = 'main/delete_object.html'
    template_name_suffix = '_confirm_delete'
    success_url = '/departments'


class DepartmentsView(LoginRequiredMixin, ListView):
    # ПРЕДСТАВЛЕНИЕ СПИСКА ОТДЕЛОВ
    context_object_name = 'departments'
    queryset = Department.objects.all()
    template_name = 'department/departments.html'
    login_url = 'login'


class SingleDepartmentView(LoginRequiredMixin, DetailView):
    # ПРДСТАВЛЕНИЕ ОДНОГО ОТДЕЛА
    model = Department
    context_object_name = 'department'
    template_name = 'department/single_department.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(SingleDepartmentView, self).get_context_data(**kwargs)
        context['department_positions'] = Position.objects.filter(department=self.object.id)
        context['departments_employees'] = Employee.objects.filter(department=self.object.id)

        # СОЗДАЁТСЯ ФОРМА С ПОЛЯМИ ВЫБОРА СОТРУДИКОВ, ИСКЛЮЧАЯ ТЕХ, КТО УЖЕ В ЭТОМ ОТДЕЛЕ
        emps = Employee.objects.exclude(department=self.get_object())
        emp_choices = [(emp, emp) for emp in emps]

        class ChoiseForma(forms.Form):
            transfer_employee_choise = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                                 choices=emp_choices,
                                                                 label='Перевести сотрудника в этот отдел')
        context['form'] = ChoiseForma
        return context
