from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class StreamingTransitionHomeView(LoginRequiredMixin, TemplateView):
    template_name = "base/streaming-transition-home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context