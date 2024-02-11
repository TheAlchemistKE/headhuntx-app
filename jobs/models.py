from django.db import models

class Job(models.Model):
    title = models.CharField(max=200)
    description = models.TextField(blank=True, null=True)
    company_name = models.CharField(max_length=150)
