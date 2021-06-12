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

    def get_data(self):
        data = {"name": self.name, "created_at": self.created_at, "owner": self.owner.id,
                "description": "", "assets": [], "strategy": {"name": "", "description": "", "parameters": []}}
        data['description'] = self.description if self.description else ""

        assets = []
        for asset in PortfolioAsset.objects.filter(portfolio_id=self.id, close_time=None):
            currency = Currency.objects.get(id=asset.currency.id)
            assets.append(
                {
                    'id': asset.id,
                    'symbol': currency.symbol,
                    'name': currency.name,
                    'status': asset.status,
                    'amount': asset.amount,
                    'apr': asset.apr,
                    'stake_start': asset.stake_start,
                    'stake_end': asset.stake_end,
                    'value': round(float(asset.amount*currency.last_price), 3),
                    'exchange': asset.exchange.name,
                    'exchange_id': asset.exchange.id,
                    'source': asset.source
                })
        data['assets'] = assets

        if not self.strategy:
            return data

        params = []
        strat_params = StrategyParameter.objects.filter(
            strategy=self.strategy)
        for param in strat_params:
            try:
                value = PortfolioParameter.objects.get(
                    portfolio=self, parameter=param).value
            except PortfolioParameter.DoesNotExist:
                value = ""
            params.append({param.parameter.name: value})

        data['strategy'] = {
            'name': self.strategy.name,
            "description": self.strategy.description,
            "parameters": params
        }

        return data

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

    class Meta:
        unique_together = [['portfolio', 'currency', 'exchange', 'status',
                            'close_time', 'stake_end', 'stake_start', 'apr']]

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    exchange = models.ForeignKey(
        Exchange, default=None, blank=True, null=True, on_delete=SET_DEFAULT)

    # None if this is a current position.
    close_time = models.DateTimeField(
        auto_now_add=False, blank=True, null=True)

    # Batch added assets for and exchange, or from bot
    BATCH = 'BATCH'
    BOT = 'BOT'
    OTHER = 'OTHER'
    SOURCE_CHOICES = (
        (BATCH, 'BATCH'),
        (BOT, 'BOT'),
        (OTHER, 'OTHER')
    )
    source = models.CharField(
        max_length=5,
        choices=SOURCE_CHOICES,
        default=OTHER
    )

    # Last time this position was updated.
    modified = models.DateTimeField(auto_now=True)

    # Instantly tradeable, tradeable with action, not tradeable.
    SPOT = 'SPOT'
    FLEX = 'FLEX'
    LOCK = 'LOCK'
    STATUS_CHOICES = (
        (SPOT, 'SPOT'),
        (FLEX, 'FLEX'),
        (LOCK, 'LOCK'),
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
        return str(self.portfolio) + "/" + status + "/" + str(self.exchange) + "/" + str(self.status) + "/" + str(self.currency)


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
    key = encrypt(models.CharField(max_length=200))
    secret = encrypt(models.CharField(
        max_length=200, blank=True, null=True))
    data = encrypt(models.CharField(
        max_length=200, blank=True, null=True))

    def __str__(self):
        return str(self.owner) + "/" + str(self.portfolio) + "/" + str(self.exchange)
