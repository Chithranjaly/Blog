from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=50)
    mission = models.TextField(max_length=2000)
    vision = models.TextField(max_length=2000)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
