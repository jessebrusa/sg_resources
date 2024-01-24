from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from .models import Apartment, Visit, Device
from .forms import DeviceForm, VisitForm, VisitHomeForm

from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone


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


class UpcomingVisitsView(ListView):
    model = Visit
    template_name = 'base/upcoming.html'

    def get_queryset(self):
        return Visit.objects.filter(date__gte=timezone.now().date(), time_completed__isnull=True).order_by('date')
    

class DeviceCreateView(CreateView):
    model = Device
    form_class = DeviceForm
    template_name = 'base/device-form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        form.instance.apartment = get_object_or_404(Apartment, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('apartment', kwargs={'pk': self.object.apartment.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apartment'] = get_object_or_404(Apartment, pk=self.kwargs['pk'])
        return context


class VisitCreateView(CreateView):
    model = Visit
    form_class = VisitForm
    template_name = 'base/visit-form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        form.instance.apartment = get_object_or_404(Apartment, pk=self.kwargs['pk'])
        form.instance.technician = f"{self.request.user.first_name} {self.request.user.last_name}"
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('apartment', kwargs={'pk': self.object.apartment.pk})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apartment'] = get_object_or_404(Apartment, pk=self.kwargs['pk'])
        return context


class VisitHomeCreateView(CreateView):
    model = Visit
    form_class = VisitHomeForm
    template_name = 'base/visit-home-form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        form.instance.apartment = form.cleaned_data.get('apartment')
        form.instance.technician = f"{self.request.user.first_name} {self.request.user.last_name}"
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('apartment', kwargs={'pk': self.object.apartment.pk})
    


#####################################################################################

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
    

class CompleteVisitCheckView(UpdateView):
    model = Visit
    fields = ['complete']

    def post(self, request, *args, **kwargs):
        visit = self.get_object()
        visit.time_completed = timezone.now()

        visit.save()
        return JsonResponse({'status': 'success'})