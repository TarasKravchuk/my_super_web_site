from . import views
from django.contrib import admin
from django.urls import path, include

app_name = 'user_app/'

urlpatterns = [
    path('registration/', views.RegistrationForm.as_view(), name='registration/'),
    path('authorization/',  views.AuthorizationForm.as_view(), name='authorization/'),
    path('logout/', views.Logout.as_view(), name='logout/'),
]

