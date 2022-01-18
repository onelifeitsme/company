from django import forms



class CreateDepartmentForm(forms.Form):
    name = forms.CharField(max_length=300, label='Название отдела')





