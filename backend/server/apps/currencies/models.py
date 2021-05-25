from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE

User = get_user_model()


class Currency(models.Model):

    class Meta:
        verbose_name_plural = 'Currencies'

    added_at = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(
        User, default=None, blank=True, null=True, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    alternative_name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    web_url = models.URLField()
    whitepaper_url = models.URLField()

    def __str__(self):
        return self.symbol


# HOURLY PRICES
class Price(models.Model):

    timestamp = models.DateTimeField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    open = models.DecimalField(max_digits=18, decimal_places=10)
    high = models.DecimalField(max_digits=18, decimal_places=10)
    low = models.DecimalField(max_digits=18, decimal_places=10)
    close = models.DecimalField(max_digits=18, decimal_places=10)
    volume = models.DecimalField(max_digits=24, decimal_places=2, default=0)

    def __str__(self):
        return str(self.currency) + "/" + str(self.timestamp)


class TagGroup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, default=None, blank=True, null=True, on_delete=models.SET_DEFAULT)
    tag_group = models.ForeignKey(
        TagGroup, default=None, blank=True, null=True, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CurrencyTag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, default=None, blank=True, null=True, on_delete=models.SET_DEFAULT)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.currency) + "/" + str(self.tag)
