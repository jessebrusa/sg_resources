from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from .models import Apartment

class StreamingTransitionHomeView(TemplateView):  # replace with your actual view class name
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