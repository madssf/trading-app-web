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
from django.contrib.auth import get_user_model


User = get_user_model()


class CurrencyBatchView(APIView):
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


class PortfolioCredentials(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        portfolios = Portfolio.objects.filter(strategy__isnull=False)
        data = []
        for p in portfolios:
            credentials = Credentials.objects.filter(portfolio=p.id)
            for cred in credentials:
                data.append(
                    {'portfolio_id': p.id, 'portfolio_name': p.name, 'user': p.owner.username, 'email': p.owner.email, 'exchange': cred.exchange.name, 'api': cred.exchange.api_url, 'key': cred.key,
                     'secret': cred.secret, 'data': cred.data})
        return JsonResponse(data, safe=False)

        '''
                portfolio_ids = [p.id]
            for cred in Credentials.objects.filter(portfolio__in=portfolio_ids):
                data[cred.portfolio.id]['credentials'][cred.exchange.name] = {
                    'key': cred.api_key, 'secret': cred.api_secret, 'payload': cred.api_payload}

            for asset in PortfolioAsset.objects.filter(portfolio__in=portfolio_ids, close_time__isnnull=True):
                if asset.exchange.name not in data[asset.portfolio.id]['assets'].keys():
                    data[asset.portfolio.id]['assets'][asset.exchange.name] = {}
                if asset.currency.name not in data[asset.portfolio.id]['assets'][asset.exchange.name].keys():
                    data[asset.portfolio.id]['assets'][asset.exchange.name][asset.currency.name] = {
                    }
                else:
                    raise KeyError(
                        'Trying to overwrite existing key - duplicate active asset.')
                # spot
                data[asset.portfolio.id]['assets'][asset.exchange.name][asset.currency.name]['spot'] = asset.spot
                # flex
                data[asset.portfolio.id]['assets'][asset.exchange.name][asset.currency.name]['flex'] = asset.flex
                # lock
                data[asset.portfolio.id]['assets'][asset.exchange.name][asset.currency.name]['locked'] = asset.locked

            for param in PortfolioParameter.objects.filter(portfolio__in=portfolio_ids):
                if param.parameter.parameter.name not in data[param.portfolio.id]['parameters'].keys():
                    data[param.portfolio.id]['parameters'][param.parameter.parameter.name] = param.value
                else:
                    raise KeyError(
                        'Trying to overwrite existing parameter - duplicate portfolio parameter.')
        except KeyError as e:
            data = {'error': e}
            '''


# for updating portfolio assets, makes a new record and sets previous Active=False
class BotPortfolioAssetList():
    permission_classes = [IsAdminUser]

    def post(self, request):
        return
