from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=200)
    skills = models.TextField()

    education = models.JSONField()
    experience = models.JSONField()
    projects = models.JSONField()
    certifications = models.JSONField()
    achievements = models.JSONField()
    languages = models.JSONField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume of {self.name}"
