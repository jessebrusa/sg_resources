from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HelloWorldView(TemplateView):
    template_name = "base/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Hello, World!'
        return context