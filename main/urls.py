from django.urls import path
# from .views import RegistrationUserView, LoginUserView, Logout, Home, DepartmentsView, PositionsView, EmployeesView, \
#     SingleEmployeeView, DepartmentCreateView, SingleDepartmentView, SinglePositionView

from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('registration', RegistrationUserView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout')
]