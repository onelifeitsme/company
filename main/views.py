from .forms import SignUpForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView, UpdateView, CreateView
from django import forms



def Home(reuqst):
    # ПРЕДСТАВЛЕНИЕ ГЛАВНОЙ СТРАНИЦЫ
    return render(reuqst, 'main/index.html')



class RegistrationUserView(FormView):
    # ПРЕДСТАВЛЕНИЕ СТРАНИЦЫ РЕГИСТРАЦИИ
    form_class = SignUpForm
    template_name = 'main/registration.html'
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super(RegistrationUserView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationUserView, self).form_invalid(form)



class LoginUserView(LoginView):
    # ПРЕДСТАВЛЕНИЕ СТРАНИЦЫ АВТОРИЗАЦИИ
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    success_url = '/'
    def get_success_url(self):
        return self.success_url



class Logout(LogoutView):
    # ПРАДСТАВЛЕНИЕ ЛОГАУТА
    next_page = '/login'



