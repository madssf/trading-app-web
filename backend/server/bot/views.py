from rest_framework.permissions import IsAdminUser
from django.db.utils import IntegrityError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.currencies.models import Currency
from rest_framework import mixins, generics
from django.http.response import JsonResponse
from rest_framework.permissions import IsAdminUser
from apps.portfolios.models import Portfolio, Credentials, PortfolioAsset, PortfolioPosition
from apps.currencies.models import Currency
from apps.exchanges.models import Exchange

from django.contrib.auth import get_user_model


User = get_user_model()


class CurrencyBotView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    permission_classes = [IsAdminUser]
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        updated = 0
        new = 0
        failed = []
        name_changed = []
        for element in request.data:
            try:
                try:

                    coin = Currency.objects.get(
                        symbol=element['symbol'])
                    # update existing
                    coin.last_price = element['last_price']
                    coin.mcap = element['mcap']
                    coin.mcap_rank = element['mcap_rank']
                    coin.pct_change_24h = element['pct_change_24h']
                    if coin.name != element['name']:
                        name_changed.append(
                            {'symbol': element['symbol'], 'name': element['name']})
                    coin.save()
                    updated += 1
                except IntegrityError:
                    failed.append(element['symbol'])
            except Currency.DoesNotExist:
                try:
                    curr = Currency.objects.create(**element)
                    curr.save()
                    new += 1
                except IntegrityError:
                    failed.append(element['symbol'])

        return Response({'updated': updated, 'new': new, 'failed': failed, 'name_changed': name_changed})


class CredentialsBotView(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        portfolios = Portfolio.objects.filter(strategy__isnull=False)
        data = []
        for p in portfolios:
            credentials = Credentials.objects.filter(portfolio=p.id)
            for cred in credentials:
                data.append(
                    {'portfolio_id': p.id, 'exchange': cred.exchange.name, 'key': cred.key, 'secret': cred.secret, 'data': cred.data})
        return JsonResponse(data, safe=False)


class ExchangeAssetsBotView(APIView):
    """
    Takes in a json object with PortfolioAssets from exchanges. Updates exisitng, opens new positions.
    """
    permission_classes = [IsAdminUser]
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        new_assets = 0
        new_positions = 0
        unchanged_positions = 0
        changed_positions = 0
        unknown_currencies = []

        for portfolio in request.data:
            for exchange in portfolio['exchanges']:
                exchange_obj = Exchange.objects.get(name=exchange['name'])
                for coin in exchange['assets']:
                    # Try to find matching currency
                    try:
                        currency = Currency.objects.get(symbol=coin['symbol'])
                    except Currency.DoesNotExist:
                        if coin['symbol'] not in unknown_currencies:
                            unknown_currencies.append(coin['symbol'])
                        continue

                    # Getting/creating asset
                    try:
                        asset = PortfolioAsset.objects.get(currency=currency)
                    except PortfolioAsset.DoesNotExist:
                        asset = PortfolioAsset.objects.create(
                            portfolio=Portfolio.objects.get(id=portfolio['portfolio']), currency=currency)
                        asset.save()
                        new_assets += 1

                    # Updating/creating position
                    try:
                        position = PortfolioPosition.objects.get(
                            asset=asset, exchange=exchange_obj, status=coin['status'])
                        amount = float(coin['amount'])
                        if float(position.amount) == amount:
                            unchanged_positions += 1
                        else:
                            position.amount = amount
                            position.save()
                            changed_positions += 1
                    except PortfolioPosition.DoesNotExist:
                        position = PortfolioPosition.objects.create(
                            asset=asset, exchange=exchange_obj, source="BOT", amount=float(coin['amount']), status=coin['status'])
                        position.save()
                        new_positions += 1

        return Response({'new_assets': new_assets, 'new_positions': new_positions, 'changed_positions': changed_positions, 'unchanged_positions': unchanged_positions, 'unknown_currencies': unknown_currencies})


class StrategyPortfoliosBotView(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request):

        portfolios = Portfolio.objects.filter(strategy__isnull=False)

        data = [
            p.get_strategy_bot_data()
            for p in portfolios]
        return JsonResponse(data, safe=False)
