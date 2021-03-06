from django.urls import path
from .views import EmployeeCreateView, load_positions, ChangeEmployeeDataView, EmployeeDeleteView, EmployeesView, \
    SingleEmployeeView

urlpatterns = [
    path('add_employee', EmployeeCreateView.as_view(), name='create_employee'),
    path('ajax/load-positions/', load_positions, name='ajax_load_positions'),
    path('change-employee-data/<slug:slug>', ChangeEmployeeDataView.as_view(), name='change_employee_data'),
    path('delete_employee/<slug:slug>', EmployeeDeleteView.as_view(), name='delete_employee'),
    path('employees', EmployeesView.as_view(), name='employees'),
    path('emp/<slug>', SingleEmployeeView.as_view(), name='single_employee'),
]
