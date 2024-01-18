from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from .models import Apartment

class StreamingTransitionHomeView(LoginRequiredMixin, TemplateView):  
    template_name = "base/streaming-transition-home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username

        total_apartments = Apartment.objects.count()
        completed_apartments = Apartment.objects.filter(complete=True).count()

        if total_apartments > 0:
            percent_completed = (completed_apartments / total_apartments) * 100
            percent_completed = round(percent_completed, 2)
        else:
            percent_completed = 0

        context['percent_completed'] = percent_completed

        return context
    

class UncompleteView(LoginRequiredMixin, ListView):
    model = Apartment
    template_name = 'base/uncomplete.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        east_apartments = Apartment.objects.filter(building='East').order_by('apartment_number')
        west_apartments = Apartment.objects.filter(building='West').order_by('apartment_number')

        context['east_apartments'] = east_apartments
        context['west_apartments'] = west_apartments

        return context