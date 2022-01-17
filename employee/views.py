from django.urls import reverse
from .forms import ChangeEmployeeDataForm, EmployeeCreateForm
from .models import Employee, Position
from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView



class EmployeeCreateView(CreateView):
    # ПРЕДСТАВЛЕНИЕ СОЗДАНИЯ СОТРУДНИКА
    model = Employee
    form_class = EmployeeCreateForm
    template_name = 'employee/create_employee.html'
    success_url = 'employees'



def load_positions(request):
    # ПОЛУЧЕНИЕ СПИСКА ДОЛЖНОСТЕЙ, ОТНОСЯЩИХСЯ К ОТДЕЛУ ПРИ СОЗДАНИИ СОТРУДИКА
    department_id = request.GET.get('department_id')
    positions = Position.objects.filter(department_id=department_id).all()
    return render(request, 'employee/position_dropdown_list_options.html', {'positions': positions})
    return JsonResponse(list(cities.values('id', 'name')), safe=False)



class ChangeEmployeeDataView(UpdateView):
    # ПРЕДСТАВЛЕНИЕ РЕДАКТИРОВАНИЯ ДАННЫХ О СОТРУДИНКЕ:
    model = Employee
    form_class = ChangeEmployeeDataForm
    template_name = 'employee/change_employee_data.html'
    success_url = '/'
    context_object_name = 'employee'



class EmployeesView(ListView):
    # ПРЕДСТАВЛЕНИЕ СПИСКА СОТРУДНИКОВ
    context_object_name = 'employees'
    queryset = Employee.objects.all()
    template_name = 'employee/employees.html'



class SingleEmployeeView(DetailView):
    # ПРЕДСТАЛВНЕИЕ ОДНОГО СОТРУДНИКА
    model = Employee
    context_object_name = 'employee'
    template_name = 'employee/single_employee.html'

