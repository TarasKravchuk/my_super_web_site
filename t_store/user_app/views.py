from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate, login as auth_login

class UserCheck(TemplateView):
    template_name = 'user_app/button.html'

    def get (self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, self.template_name)


class AuthorizationForm (FormView):
    form_class = AuthenticationForm
    template_name = 'user_app/authorization.html'
    success_url = '/'
    def form_valid (self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(AuthorizationForm, self).form_valid(form)


class RegistrationForm (FormView):
    form_class = UserCreationForm
    success_url = '/auth-urls/authorization/'
    template_name = 'user_app/registration.html'

    def form_valid (self, form):
        form.save()
        return super (RegistrationForm, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegistrationForm, self).form_invalid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')
