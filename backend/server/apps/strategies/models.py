from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Strategy(models.Model):
    class Meta:
        verbose_name_plural = 'Strategies'
    created_by = models.ForeignKey(
        User, default=User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ParameterType(models.Model):
    created_by = models.ForeignKey(
        User, default=User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Parameter(models.Model):
    created_by = models.ForeignKey(
        User, default=User, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    parameter_type = models.ForeignKey(ParameterType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StrategyParameter(models.Model):
    class Meta:
        unique_together = [['parameter', 'strategy']]

    created_by = models.ForeignKey(
        User, default=User, blank=True, null=True, on_delete=models.SET_NULL)
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.strategy) + "/" + str(self.parameter)
