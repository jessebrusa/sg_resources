from django.shortcuts import render
from django.views.generic import TemplateView


class Directory(TemplateView):
    template_name = "base/directory.html"