from .forms import CreateDepartmentForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from employee.models import Employee

from .models import Department
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView
from django import forms



class DepartmentCreateView(FormView):
    # ПРЕДСТАВЛЕНИЕ СОЗДАНИЯ ОТДЕЛА
    form_class = CreateDepartmentForm
    template_name = 'department/create_department.html'
    success_url = 'departments'
    #
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_department_name = form.cleaned_data['name']
            print(new_department_name)
            print(type(new_department_name))
            transfer_employee_choice = form.cleaned_data['transfer_employee_choise']
            print(transfer_employee_choice)
            form.save()
            print(Department.objects.all())
            new_department = Department.objects.get(name=new_department_name)
            for emp in transfer_employee_choice:
                emp = Employee.objects.get(username=emp)
                emp.department = new_department
                emp.save()
        else:
            print('ploho')
        return HttpResponse('sdfsf')



class DepartmentsView(ListView):
    # ПРЕДСТАВЛЕНИЕ СПИСКА ОТДЕЛОВ
    context_object_name = 'departments'
    queryset = Department.objects.all()
    template_name = 'department/departments.html'



class SingleDepartmentView(DetailView):
    # ПРДСТАВЛЕНИЕ ОДНОГО ОТДЕЛА
    model = Department
    context_object_name = 'department'
    template_name = 'department/single_department.html'

    def get_context_data(self, **kwargs):
        context = super(SingleDepartmentView, self).get_context_data(**kwargs)
        context['departments_employees'] = Employee.objects.filter(department=self.object.id)

        # СОЗДАЁТСЯ ФОРМА С ПОЛЯМИ ВЫБОРА СОТРУДИКОВ, ИСКЛЮЧАЯ ТЕХ, КТО УЖЕ В ЭТОМ ОТДЕЛЕ
        emps = Employee.objects.exclude(department=self.get_object())
        emp_choices = [(emp, emp) for emp in emps]
        class ChoiseForma(forms.Form):
            transfer_employee_choise = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=emp_choices, label='Перевести сотрудника в этот отдел')
        context['form'] = ChoiseForma
        return context


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            employees_to_add = request.POST.getlist('transfer_employee_choise')
            department = self.get_object()
            for emp in employees_to_add:
                emp = Employee.objects.get(username=emp)
                emp.department = department
                emp.save()
            return HttpResponseRedirect(self.request.path_info)




