from apps.portfolios.models import PortfolioAsset
from rest_framework.permissions import IsAdminUser
from django.db.utils import IntegrityError
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.currencies.models import Currency
from rest_framework import mixins, generics
from django.http.response import JsonResponse
from rest_framework.permissions import IsAdminUser
from apps.portfolios.models import Portfolio, Credentials
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
    Takes in a json object with PortfolioAssets from exchanges and updates, closes, opens new positions.
    """
    permission_classes = [IsAdminUser]
    parser_classes = [JSONParser]

    def post(self, request, format=None):
        failed = 0
        new = 0
        updated = []
        unknown_currencies = []

        for portfolio in request.data:
            # return Response({'data': portfolio.keys()})
            for exchange in portfolio['exchanges']:
                for coin in exchange['assets']:
                    try:
                        currency = Currency.objects.get(symbol=coin['symbol'])
                        asset = PortfolioAsset.objects.get(
                            close_time=None, portfolio=portfolio['portfolio'], exchange=Exchange.objects.get(name=exchange['name']), currency=currency)
                        updated.append(str(asset))
                        # self.handle_update_asset(asset, exchane)

                    except (Currency.DoesNotExist, PortfolioAsset.DoesNotExist):
                        try:
                            asset_obj = PortfolioAsset.objects.create(
                                portfolio=Portfolio.objects.get(id=portfolio['portfolio']), exchange=Exchange.objects.get(name=exchange['name']), currency=Currency.objects.get(symbol=coin['symbol']),
                                amount=coin['amount'],
                                status=coin['status']
                            )
                            asset_obj.save()
                            new += 1
                        except (Currency.DoesNotExist):
                            failed += 1
                            unknown_currencies.append(coin['symbol'])

        return Response({'updated': updated, 'new': new, 'failed': failed, 'unknowns': unknown_currencies})


#        return Response({'data': data})
