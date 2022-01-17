from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from employee.models import Employee
from .models import Position
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView
from django import forms



class PositionCreateView(CreateView):
    # ПРЕДСТАВЛЕНИЕ СОЗДАНИЯ ДОЛЖНОСТИ
    model = Position
    fields = ['department', 'name', 'description']
    template_name = 'position/create_position.html'
    success_url = 'positions'



class PositionChangeView(UpdateView):
    # ПРЕДСТАВЛЕНИЕ РЕДАКТИРОВАНИЯ ДОЛЖНОСТИ
    model = Position
    fields = ['name', 'description']
    template_name = 'main/create_position.html'
    template_name_suffix = '_update_form'



class PositionsView(ListView):
    # ПРЕДСТАВЛЕНИЕ СПИСКА ДОЛЖНОСТЕЙ
    context_object_name = 'positions'
    queryset = Position.objects.order_by('department')
    template_name = 'position/positions.html'



class SinglePositionView(DetailView):
    # ПРЕДСТАВЛЕНИЕ ОДНОЙ ДОЛЖНОСТИ
    model = Position
    context_object_name = 'position'
    template_name = 'position/single_position.html'

    def get_context_data(self, **kwargs):
        context = super(SinglePositionView, self).get_context_data(**kwargs)
        context['position_employees'] = Employee.objects.filter(position=self.object.id)

        # СОЗДАЁТСЯ ФОРМА С ПОЛЯМИ ВЫБОРА СОТРУДИКОВ, ИСКЛЮЧАЯ ТЕХ, КТО УЖЕ В ЭТОМ ОТДЕЛЕ
        emps = Employee.objects.exclude(position=self.get_object())
        emp_choices = [(emp, emp) for emp in emps]
        class ChoiseForma(forms.Form):
            transfer_employee_choise = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
            choices=emp_choices, label='Перевести сотрудника на эту должность')
        context['form'] = ChoiseForma
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            employees_to_add = request.POST.getlist('transfer_employee_choise')
            position = self.get_object()
            print(type(position))
            for emp in employees_to_add:
                emp = Employee.objects.get(username=emp)
                emp.position = position
                emp.save()
            return HttpResponseRedirect(self.request.path_info)







