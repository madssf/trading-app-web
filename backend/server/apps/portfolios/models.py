from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import SET_DEFAULT
from django_cryptography.fields import encrypt
from apps.strategies.models import Strategy, StrategyParameter
from apps.exchanges.models import Exchange
from apps.currencies.models import Currency

User = get_user_model()


class Portfolio(models.Model):
    class Meta:
        unique_together = [['owner', 'name']]
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
    class Meta:
        unique_together = [['portfolio', 'parameter']]
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    parameter = models.ForeignKey(StrategyParameter, on_delete=models.CASCADE)
    value = models.TextField()

    def __str__(self):
        return str(self.portfolio) + "/" + str(self.parameter)


class PortfolioAsset(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    exchange = models.ForeignKey(
        Exchange, default=None, blank=True, null=True, on_delete=SET_DEFAULT)

    # None if this is a current position.
    close_time = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)
    # Last time this position was updated.
    modified = models.DateTimeField(auto_now=True)
    # Constants in Model class
    SPOT = 'SPOT'
    FLEX = 'FLEX'
    LOCK = 'LOCK'
    STATUS_CHOICES = (
        (SPOT, 'Instantly tradeable'),
        (FLEX, 'Tradeable with action'),
        (LOCK, 'Not tradeable'),
    )
    status = models.CharField(
        max_length=4,
        choices=STATUS_CHOICES,
        default=SPOT,
    )

    amount = models.DecimalField(
        max_digits=18, decimal_places=10, blank=True, null=True)

    # staking info
    apr = models.DecimalField(
        max_digits=7, decimal_places=4, default=0, blank=True, null=True)
    stake_start = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)
    stake_end = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)

    def __str__(self):
        status = "OPEN" if not self.close_time else "CLOSED"
        return str(self.portfolio) + "/" + status + "/" + str(self.exchange) + "/" + str(self.currency) + "/" + str(self.status)


class PortfolioLogEntry(models.Model):
    class Meta:
        verbose_name_plural = 'Portfolio log entries'
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    '''
    [{'symbol': symbol, 'amount': amount, 'apr': apr}, ...]
    '''
    assets = models.JSONField()


class Trade(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    exchange = models.ForeignKey(
        Exchange, default=None, blank=True, null=True, on_delete=SET_DEFAULT)
    buy_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name='buy_currency')
    sell_currency = models.ForeignKey(
        Currency, on_delete=models.CASCADE, related_name='sell_currency')
    buy_amount = models.DecimalField(max_digits=18, decimal_places=10)
    sell_amount = models.DecimalField(max_digits=18, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.portfolio}/{self.buy_currency}/{self.sell_currency}/{self.timestamp}"


class Deposit(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=18, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.portfolio}/{self.currency}/{self.timestamp}"


class Credentials(models.Model):
    class Meta:
        verbose_name_plural = 'Credentials'
        unique_together = [['owner', 'exchange', 'portfolio']]

    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    api_key = encrypt(models.CharField(max_length=200))
    api_secret = encrypt(models.CharField(
        max_length=200, blank=True, null=True))
    api_payload = encrypt(models.CharField(
        max_length=200, blank=True, null=True))

    def __str__(self):
        return str(self.owner) + "/" + str(self.portfolio) + "/" + str(self.exchange)
