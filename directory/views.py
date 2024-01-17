from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class Directory(LoginRequiredMixin, TemplateView):
    template_name = "base/directory.html"


class UserLoginView(LoginView):
    template_name = 'base/login.html'


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('directory')