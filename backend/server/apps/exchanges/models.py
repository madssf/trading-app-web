from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Exchange(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User, default=User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    web_url = models.URLField(unique=True)
    api_url = models.URLField(unique=True)

    def __str__(self):
        return self.name
