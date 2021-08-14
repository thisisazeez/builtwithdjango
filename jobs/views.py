from datetime import datetime, timedelta

from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from .models import Job
from .forms import PostJob
from newsletter.views import NewsletterSignupForm


class JobListView(ListView):
    model = Job
    template_name = "jobs/all_jobs.html"
    filter_date = datetime.today() - timedelta(days=31)
    queryset = Job.objects.filter(created_datetime__gte=filter_date).filter(
        approved=True
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newsletter_form"] = NewsletterSignupForm

        return context


class JobDetailView(DetailView):
    model = Job
    template_name = "jobs/job_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newsletter_form"] = NewsletterSignupForm

        return context


class JobCreateView(CreateView):
    model = Job
    form_class = PostJob
    template_name = "jobs/post-job.html"
    success_url = reverse_lazy("job-thank-you")


class ThankYouView(TemplateView):
    template_name = "jobs/post-job-thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newsletter_form"] = NewsletterSignupForm

        return context
