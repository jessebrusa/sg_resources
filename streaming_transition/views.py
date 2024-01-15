from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class LandingPageView(TemplateView):
    template_name = "base/landing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello, World!'
        return context