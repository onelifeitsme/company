from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from employee.models import Employee
from .models import Position
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django import forms


class PositionCreateView(LoginRequiredMixin, CreateView):
    # ПРЕДСТАВЛЕНИЕ СОЗДАНИЯ ДОЛЖНОСТИ
    model = Position
    fields = ['department', 'name', 'description']
    template_name = 'position/create_position.html'
    success_url = 'positions'
    login_url = 'login'


class PositionChangeView(LoginRequiredMixin, UpdateView):
    # ПРЕДСТАВЛЕНИЕ РЕДАКТИРОВАНИЯ ДОЛЖНОСТИ
    model = Position
    fields = ['name', 'description']
    template_name = 'position/create_position.html'
    template_name_suffix = '_update_form'
    login_url = 'login'


class PositionDeleteView(DeleteView):
    # ПРЕДСТАВЛЕНИЕ УДАЛЕНИЯ ДОЛЖНОСТИ
    model = Position
    template_name = 'main/delete_object.html'
    template_name_suffix = '_confirm_delete'
    success_url = '/positions'


class PositionsView(LoginRequiredMixin, ListView):
    # ПРЕДСТАВЛЕНИЕ СПИСКА ДОЛЖНОСТЕЙ
    context_object_name = 'positions'
    queryset = Position.objects.order_by('department')
    template_name = 'position/positions.html'
    login_url = 'login'


class SinglePositionView(LoginRequiredMixin, DetailView):
    # ПРЕДСТАВЛЕНИЕ ОДНОЙ ДОЛЖНОСТИ
    model = Position
    context_object_name = 'position'
    template_name = 'position/single_position.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(SinglePositionView, self).get_context_data(**kwargs)
        context['position_employees'] = Employee.objects.filter(position=self.object.id)

        # СОЗДАЁТСЯ ФОРМА С ПОЛЯМИ ВЫБОРА СОТРУДИКОВ, ИСКЛЮЧАЯ ТЕХ, КТО УЖЕ В ЭТОМ ОТДЕЛЕ
        emps = Employee.objects.exclude(position=self.get_object())
        emp_choices = [(emp, emp.last_name) for emp in emps]

        class ChoiseForma(forms.Form):
            transfer_employee_choise = forms.ChoiceField(choices=emp_choices,
                                                         label='Перевести сотрудника на эту должность')
        context['form'] = ChoiseForma
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            employee_to_add = request.POST.get('transfer_employee_choise')
            position = self.get_object()
            emp = Employee.objects.get(last_name=employee_to_add)
            emp.position = position
            emp.department = position.department
            emp.save()
            position.vacant = False
            position.save()
            return HttpResponseRedirect(self.request.path_info)
