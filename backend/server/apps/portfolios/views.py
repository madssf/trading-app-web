from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, generics
from django.http.response import JsonResponse
from apps.users.permissions import OwnerCUD_AuthR
from rest_framework.permissions import IsAdminUser
from django.db.models import Q

from .models import Deposit, Portfolio, PortfolioAsset, PortfolioLogEntry, PortfolioParameter, Trade, Credentials
from .serializers import DepositSerializer, PortfolioAssetSerializer, PortfolioLogEntrySerializer, PortfolioSerializer, PortfolioParameterSerializer, TradeSerializer, CredentialsSerializer
from apps.currencies.models import Currency
from apps.strategies.models import Parameter

User = get_user_model()


class PortfolioViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()

    def get_permissions(self):
        return OwnerCUD_AuthR(self, super())

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(Q(owner=self.request.user) | Q(public=True))


class PortfolioParameterViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioParameterSerializer
    queryset = PortfolioParameter.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class PortfolioLogEntryViewSet(viewsets.ModelViewSet):

    serializer_class = PortfolioLogEntrySerializer
    queryset = PortfolioLogEntry.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class PortfolioAssetView(viewsets.ModelViewSet):

    serializer_class = PortfolioAssetSerializer
    queryset = PortfolioAsset.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class TradeViewSet(viewsets.ModelViewSet):

    serializer_class = TradeSerializer
    queryset = Trade.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class DepositViewSet(viewsets.ModelViewSet):

    serializer_class = DepositSerializer
    queryset = Deposit.objects.all()

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        return self.queryset.all()


class CredentialsViewSet(viewsets.ModelViewSet):

    serializer_class = CredentialsSerializer
    queryset = Credentials.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class BotPortfolioList(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = [IsAdminUser]

    # fix, not workinng with new portfolioasset
    def get(self, request):
        try:
            portfolios = Portfolio.objects.filter(strategy__isnull=False)
            portfolio_ids = []
            data = {}
            for p in portfolios:
                data[p.id] = {'strategy': p.strategy.name,
                              'credentials': {}, 'parameters': {}, 'assets': {}}
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
        return JsonResponse(data)


# for updating portfolio assets, makes a new record and sets previous Active=False
class BotPortfolioAssetList():
    permission_classes = [IsAdminUser]

    def post(self, request):
        return

# user home portfolio view


def PortfolioID(request, id):
    portfolio = Portfolio.objects.filter(owner=request.user, id=id).values()[0]
    asset_qs = PortfolioAsset.objects.filter(
        portfolio_id=id, active=True).values()
    assets = []
    for asset in asset_qs:
        currency = Currency.objects.filter(id=asset['currency_id'])[0]
        sums = {'locked': asset['locked'],
                'spot': asset['spot'], 'flex':  asset['flex'], 'tot': 0}
        for element in sums.keys():
            if sums[element] == None:
                sums[element] = 0
            else:
                sums['tot'] += sums[element]

        assets.append(
            {
                'name': currency,  # ['name'],
                'total': round(sums['tot'], 2),
                'data': {'average': round(asset['average'], 2)

                         }

            }
        )
    params_qs = PortfolioParameter.objects.filter().values()
    parameters = []
    for param in params_qs:
        parameters.append({Parameter.objects.filter(
            id=param['parameter_id'])[0].name: param['value']})
       # parameters.append({Parameter.objects.filter().values()})

   # print(assets)
    context = {
        'name': portfolio['name'],
        "id": portfolio['id'],
        "assets": assets,
        "parameters": parameters
    }
    return JsonResponse(context)
