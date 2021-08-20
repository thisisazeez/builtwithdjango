from django.db import models
from django.urls import reverse


class Job(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    listing_url = models.URLField(unique=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    salary = models.IntegerField(blank=True, null=True)

    company = models.ForeignKey(
        "Company", on_delete=models.CASCADE, related_name="jobs"
    )

    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_datetime"]

    def __str__(self):
        return f"{self.company}: {self.title}"

    def get_absolute_url(self):
        return reverse("job_details", args=[self.pk])


class Company(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100, unique=True)
    url = models.URLField(unique=True)
    logo = models.ImageField(upload_to="company_logo/")
    email = models.EmailField(blank=True)

    project = models.OneToOneField(
        "projects.Project", on_delete=models.CASCADE, blank=True, null=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"
