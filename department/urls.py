from django.urls import path
from .views import *

urlpatterns = [
    path('departments', DepartmentsView.as_view(), name='departments'),
    path('create_department', DepartmentCreateView.as_view(), name='create_department'),
    path('dep/<slug>', SingleDepartmentView.as_view(), name='single_department'),

]