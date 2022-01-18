from django.urls import path
from .views import *

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('registration', RegistrationUserView.as_view(), name='registration'),
    path('login', LoginUserView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),

]