from services.is_stablecoin import is_stablecoin
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import SET_DEFAULT
from django_cryptography.fields import encrypt

from apps.strategies.models import Strategy, StrategyParameter
from apps.exchanges.models import Exchange
from apps.currencies.models import Currency, Tag, TagGroup, CurrencyTag

import datetime
from django.forms.models import model_to_dict


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
    instructions = models.JSONField(default=None, blank=True, null=True)
    balanced_portfolio = models.JSONField(default=None, blank=True, null=True)
    diff_matrix = models.JSONField(default=None, blank=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    public = models.BooleanField(default=False)

    def get_frontend_detail_data(self):

        data = {"id": self.id, "name": self.name, "created_at": self.created_at, "owner": self.owner.id,"description": "", "assets": [], "deposits": [], "trades": [], "stats": {}, "strategy": {"id": "", "name": "", "description": "", "parameters": []}}
        
        data['description'] = self.description if self.description else ""
        data['assets'] = [asset.get_asset_data() for asset in PortfolioAsset.objects.filter(portfolio_id=self.id)]
        data['deposits'] = list(model_to_dict(d) for d in Deposit.objects.filter(portfolio_id=self.id))
        data['trades'] = list(model_to_dict(t) for t in Trade.objects.filter(portfolio_id=self.id))
        data['stats']['deposit_total'] = sum(d['amount'] for d in data['deposits'])

        # STRATEGY
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
            "parameters": params,
            "instructions": self.instructions, 
            'balanced_portfolio': self.balanced_portfolio, 
            "diff_matrix": self.diff_matrix,
        }

        return data

    def get_strategy_bot_data(self):
        data = {
            "id": self.id,
            "name": self.name,
            "owner": self.owner.id,
            "email": self.owner.email,
            'execute_trades': self.bot_execute_trades,
            'email_notify': self.bot_email_notify,
            "assets": {},
            "strategy": {
                'id': self.strategy.id,
                'name': self.strategy.name,
                'parameters': {},
                'instructions' : self.instructions,
                'balanced_portfolio': self.balanced_portfolio,
                'diff_matrix': self.diff_matrix,
                'modified': self.modified,
            }
        }
        for asset in PortfolioAsset.objects.filter(portfolio_id=self.id):
            data['assets'][asset.currency.symbol] = asset.get_asset_data()

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
                    try:
                        symbols += [c.currency.symbol for c in CurrencyTag.objects.filter(
                            tag=Tag.objects.get(tag_group=TagGroup.objects.get(name=tag)))]
                    except (CurrencyTag.DoesNotExist, Tag.DoesNotExist, TagGroup.DoesNotExist):
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

    def get_asset_positions_list(self):
        return list(
            {
                'id': position.id,
                'status': position.status,
                'amount': position.amount,
                'apr': position.apr,
                'stake_start': position.stake_start,
                'stake_end': position.stake_end,
                'value': round(float(position.amount*position.asset.currency.last_price), 3),
                'exchange': position.exchange.name,
                'exchange_id': position.exchange.id,
                'source': position.source,
            } for position in PortfolioPosition.objects.filter(asset=self))

    def get_asset_data(self):
        positions = self.get_asset_positions_list()
        return {
            'id': self.id,
            'symbol': self.currency.symbol,
            'name': self.currency.name,
            'last_price': self.currency.last_price,
            'pct_change_24h': self.currency.pct_change_24h,
            'average': self.average,
            'value': sum(position['value'] for position in positions),
            'amount': sum(float(position['amount']) for position in positions),
            'positions': positions}

    def update_average(self, amount, price):
        if is_stablecoin(self):
            return
        if self.average:
            prev_amt = sum(x['amount'] for x in self.get_asset_positions_list())
            self.average = ((price*amount)+(self.average*prev_amt))/(amount+prev_amt)
            self.save()
        else:
            self.average = price
            self.save()

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
    amount = models.DecimalField(max_digits=18, decimal_places=10)
    price = models.DecimalField(max_digits=18, decimal_places=10)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.portfolio}/{self.buy_currency}/{self.sell_currency}/{self.timestamp}"


class Deposit(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    exchange = models.ForeignKey(Exchange, default=None, blank=True, null=True, on_delete=SET_DEFAULT)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=18, decimal_places=10)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

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
