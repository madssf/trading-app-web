from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import SET_DEFAULT
from apps.strategies.models import Strategy, StrategyParameter


User = get_user_model()


class Portfolio(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    strategy = models.ForeignKey(
        Strategy, default=None, blank=True, null=True, on_delete=SET_DEFAULT)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + "/" + self.name


class PortfolioParameter(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    parameter = models.ForeignKey(StrategyParameter, on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return str(self.portfolio) + "/" + str(self.parameter)
