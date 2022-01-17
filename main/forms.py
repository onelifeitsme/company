from django.contrib.auth.forms import UserCreationForm
from employee.models import Employee



class SignUpForm(UserCreationForm):
   class Meta:
      model = Employee
      fields = ('username', 'last_name', 'position', 'department',)
