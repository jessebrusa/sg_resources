from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View


class LandingPageView(LoginRequiredMixin, TemplateView):
    template_name = "base/landing-page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
    

class UserLoginView(LoginView):
    template_name = 'base/login.html'


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('landing-page')