from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ChangeEmployeeDataForm, EmployeeCreateForm
from .models import Employee, Position
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    """Представление страницы создания сотрудника"""
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'employee/create_employee.html'
    success_url = 'employees'
    login_url = 'login'


def load_positions(request):
    """Получение списка должностей, относящихся к отделу, при создании сотрудника"""
    department_id = request.GET.get('department_id')
    positions = Position.objects.filter(department_id=department_id, vacant=True).all()
    return render(request, 'employee/position_dropdown_list_options.html', {'positions': positions})


class ChangeEmployeeDataView(LoginRequiredMixin, UpdateView):
    """Представление страницы редактирования данных о сотруднике"""
    model = Employee
    form_class = ChangeEmployeeDataForm
    template_name = 'employee/change_employee_data.html'
    context_object_name = 'employee'
    login_url = 'login'


class EmployeeDeleteView(DeleteView):
    """Представление удаления сотрудника"""
    model = Employee
    template_name = 'main/delete_object.html'
    template_name_suffix = '_confirm_delete'
    success_url = '/employees'


class EmployeesView(LoginRequiredMixin, ListView):
    """Представление страницы спика сотрудников"""
    context_object_name = 'employees'
    queryset = Employee.objects.all()
    template_name = 'employee/employees.html'
    login_url = 'login'

    def get_success_url(self):
        return self.get_object()


class SingleEmployeeView(LoginRequiredMixin, DetailView):
    """Представление страницы одного сотрудника"""
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee/single_employee.html'
    login_url = 'login'
