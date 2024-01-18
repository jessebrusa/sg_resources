from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from .models import Apartment

from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib import messages

from datetime import date


class ApartmentDetailView(DetailView):
    model = Apartment
    context_object_name = 'apartment'
    template_name = 'base/details.html' 

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('visits', 'devices')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        apartment = self.object
        context['devices'] = apartment.devices.all()
        context['visits'] = apartment.visits.all()
        return context


class StreamingTransitionHomeView(LoginRequiredMixin, TemplateView):  
    template_name = "base/streaming-transition-home.html"

    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search', None)
        if search_query is not None:
            try:
                apartment = Apartment.objects.get(apartment_number=search_query)
                return redirect('apartment', pk=apartment.id)
            except Apartment.DoesNotExist:
                messages.add_message(request, messages.INFO, 'No apartment found with that number.')
        return super().get(request, *args, **kwargs)


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

        east_apartments = Apartment.objects.filter(building='East', complete=False).order_by('apartment_number')
        west_apartments = Apartment.objects.filter(building='West', complete=False).order_by('apartment_number')

        context['east_apartments'] = east_apartments
        context['west_apartments'] = west_apartments

        return context
    

class CompleteView(LoginRequiredMixin, ListView):
    model = Apartment
    template_name = 'base/complete.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        east_apartments = Apartment.objects.filter(building='East', complete=True).order_by('apartment_number')
        west_apartments = Apartment.objects.filter(building='West', complete=True).order_by('apartment_number')

        context['east_apartments'] = east_apartments
        context['west_apartments'] = west_apartments

        return context


class CompleteApartmentCheckView(UpdateView):
    model = Apartment
    fields = ['complete']

    def post(self, request, *args, **kwargs):
        apartment = self.get_object()
        apartment.complete = True
        apartment.date_completed = date.today()
        apartment.save()
        return JsonResponse({'status': 'success'})
    

class NotCompleteApartmentCheckView(UpdateView):
    model = Apartment
    fields = ['complete']

    def post(self, request, *args, **kwargs):
        apartment = self.get_object()
        apartment.complete = False
        apartment.date_completed = None
        apartment.save()
        return JsonResponse({'status': 'success'})