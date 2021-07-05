from django.db import models

class Project(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    live_demo_link = models.CharField(max_length=200, blank=True)
    github_page_link = models.URLField(blank=True)
    description = models.TextField()
    technologies = models.TextField()
