from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

