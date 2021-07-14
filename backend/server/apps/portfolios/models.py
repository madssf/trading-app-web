from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import SET_DEFAULT
from django_cryptography.fields import encrypt
from apps.strategies.models import Strategy, StrategyParameter
from apps.exchanges.models import Exchange
from apps.currencies.models import Currency, Tag, CurrencyTag

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
    bot_execute_trades = models.BooleanField(default=False)
    bot_email_notify = models.BooleanField(default=False)
    public = models.BooleanField(default=False)

    def get_detail_view_data(self):
        data = {"id": self.id, "name": self.name, "created_at": self.created_at, "owner": self.owner.id,
                "description": "", "assets": [], "strategy": {"id": "", "name": "", "description": "", "parameters": []}}
        data['description'] = self.description if self.description else ""

        assets = []
        for asset in PortfolioAsset.objects.filter(portfolio_id=self.id):
            assets.append(
                {
                    'id': asset.id,
                    'symbol': asset.currency.symbol,
                    'name': asset.currency.name,
                    'last_price': asset.currency.last_price,
                    'pct_change_24h': asset.currency.pct_change_24h,
                    'avg': asset.average,
                    'positions':  list(
                        {'status': position.status,
                         'amount': position.amount,
                         'apr': position.apr,
                         'stake_start': position.stake_start,
                         'stake_end': position.stake_end,
                         'value': round(float(position.amount*position.asset.currency.last_price), 3),
                         'exchange': position.exchange.name,
                         'exchange_id': position.exchange.id,
                         'source': position.source,
                         } for position in PortfolioPosition.objects.filter(asset=asset)),
                })
        data['assets'] = assets

        if not self.strategy:
            return data

        params = []
        strat_params = StrategyParameter.objects.filter(
            strategy=self.strategy)
        for param in strat_params:
            try:
                pf_param = PortfolioParameter.objects.get(
                    portfolio=self, parameter=param)
                pf_param_value = pf_param.value
                pf_param_id = pf_param.id
            except PortfolioParameter.DoesNotExist:
                pf_param_value = None
                pf_param_id = None
            params.append({"name": param.parameter.name, "description": param.parameter.description,
                          "type": param.parameter.parameter_type.name,
                           "strat_param_id": param.parameter.id, "value": pf_param_value, "pf_param_id": pf_param_id})

        data['strategy'] = {
            'id': self.strategy.id,
            'name': self.strategy.name,
            "description": self.strategy.description,
            "parameters": params
        }

        return data

    def get_strategy_bot_data(self):
        data = {
            "id": self.id,
            "name": self.name,
            "owner": self.owner.id,
            'execute_trades': self.bot_execute_trades,
            'email_notify': self.bot_email_notify,
            "assets": {},
            "strategy": {
                'id': self.strategy.id,
                'name': self.strategy.name,
                'parameters': {}
            }
        }
        for asset in PortfolioAsset.objects.filter(portfolio_id=self.id):
            position = {
                'status': asset.status,
                'amount': asset.amount,
                'value': round(float(asset.amount*asset.currency.last_price), 3),
                'exchange': asset.exchange.name
            }
            symbol = asset.currency.symbol
            if symbol not in data['assets'].keys():
                data['assets'][symbol] = [position]
            else:
                data['assets'][symbol].append(position)

        for param in StrategyParameter.objects.filter(strategy=self.strategy):
            try:
                value = PortfolioParameter.objects.get(
                    portfolio=self, parameter=param
                ).value
            except PortfolioParameter.DoesNotExist:
                value = None
            data['strategy']['parameters'][param.parameter.name] = value
        # getting banned coins from tags
        try:
            tags = data['strategy']['parameters']['banned_tags'].split(",")
            symbols = []
            for tag in tags:
                try:
                    symbols += [c.currency.symbol for c in CurrencyTag.objects.filter(
                        tag=Tag.objects.get(name=tag))]
                except (CurrencyTag.DoesNotExist, Tag.DoesNotExist):
                    pass
            if data['strategy']['parameters']['banned']:
                data['strategy']['parameters']['banned'] += ',' + \
                    ','.join(symbols)
            else:
                data['strategy']['parameters']['banned'] = ','.join(symbols)
        except (KeyError, AttributeError):
            pass

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
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    average = models.DecimalField(
        max_digits=18, decimal_places=10, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.portfolio) + "/" + str(self.currency)


class PortfolioPosition(models.Model):

    class Meta:
        unique_together = [['asset', 'exchange',
                            'status', 'stake_end', 'stake_start', 'apr']]

    asset = models.ForeignKey(PortfolioAsset, on_delete=models.CASCADE)
    exchange = models.ForeignKey(
        Exchange, default=None, blank=True, null=True, on_delete=SET_DEFAULT)

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
        return str(self.asset) + "/" + str(self.exchange) + "/" + str(self.status)


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
