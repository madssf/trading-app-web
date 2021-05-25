from django.db import models
from django.contrib.auth import get_user_model
from django_cryptography.fields import encrypt
from apps.portfolios.models import Portfolio

User = get_user_model()


class Exchange(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User, default=None, blank=True, null=True, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    web_url = models.URLField()
    api_url = models.URLField()

    def __str__(self):
        return self.name


class Credentials(models.Model):

    class Meta:
        verbose_name_plural = 'Credentials'

    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    api_key = encrypt(models.CharField(max_length=200))
    api_secret = encrypt(models.CharField(max_length=200))
    api_payload = encrypt(models.CharField(max_length=200))

    def __str__(self):
        return str(self.owner) + "/" + str(self.portfolio) + "/" + str(self.exchange)
