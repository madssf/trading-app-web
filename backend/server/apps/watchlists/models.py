from django.db import models
from django.contrib.auth import get_user_model
from apps.currencies.models import Currency


User = get_user_model()


class Watchlist(models.Model):
    class Meta:
        unique_together = [['owner', 'name']]
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + "/" + self.name


class WatchlistCurrency(models.Model):
    class Meta:
        verbose_name_plural = 'Watchlist currencies'
        unique_together = ['watchlist', 'currency']
    added_at = models.DateTimeField(auto_now_add=True)
    watchlist = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.watchlist) + "/" + str(self.currency)
