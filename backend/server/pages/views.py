from .parsers import AssetBatchParser
from django.shortcuts import render
from apps.portfolios.models import Portfolio, PortfolioAsset, PortfolioParameter
from apps.currencies.models import Currency
from apps.strategies.models import Strategy, Parameter
from apps.exchanges.models import Exchange
from django.http.response import JsonResponse
from rest_framework import mixins, generics, permissions
from django.views.generic.edit import DeleteView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView


def MyPortfoliosView(request):
    # create a dictionary
    portfolios = Portfolio.objects.filter(owner=request.user)
    context = {
        "data": portfolios,
    }
    # return response
    return render(request, "my_portfolios.html", context)


class MyPortfolioID(mixins.ListModelMixin, generics.GenericAPIView):

    def get(self, request, id):

        portfolio = Portfolio.objects.get(
            id=id, owner=request.user)
        asset_qs = PortfolioAsset.objects.filter(
            portfolio_id=portfolio.id, close_time=None).values()
        assets = []
        for asset in asset_qs:
            currency = Currency.objects.get(id=asset['currency_id'])
            assets.append(
                {
                    'id': asset['id'],
                    'symbol': currency.symbol,
                    'name': currency.name,
                    'status': asset['status'],
                    'amount': asset['amount'],
                    'apr': asset['apr'],
                    'stake_start': asset['stake_start'],
                    'stake_end': asset['stake_end'],
                    'value': round(float(asset['amount']*currency.last_price), 3),
                    'exchange': asset['exchange_id'],
                    'source': asset['source']
                }
            )
        params_qs = PortfolioParameter.objects.filter(
            portfolio=portfolio.id).values()
        parameters = []
        for param in params_qs:
            parameters.append({Parameter.objects.filter(
                id=param['parameter_id'])[0].name: param['value']})
        try:
            strategy_name = Strategy.objects.get(id=portfolio.strategy.id).name
        except AttributeError as e:
            strategy_name = "No strategy"
        data = {
            'name': portfolio.name,
            "id": portfolio.name,
            "assets": assets,
            "strategy": strategy_name,
            "parameters": parameters
        }
        return JsonResponse(data, safe=False)


class DeleteAssetView(DeleteView):

    model = PortfolioAsset

    # can specify success url
    # url to redirect after sucessfully
    # deleting object
    success_url = "/"


class BatchAddAssetsView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    permission_classes = [permissions.IsAuthenticated]
    #parser_classes = [JSONParser]

    def post(self, request, portfolio_id, exchange_id, format=None):

        try:
            portfolio = Portfolio.objects.get(id=portfolio_id)
        except Portfolio.DoesNotExist:
            return Response({'message': 'unknown portfolio'})
        try:
            exchange = Exchange.objects.get(id=exchange_id)
        except Exchange.DoesNotExist:
            return Response({'message': 'unknown exchange'})
        parsed = AssetBatchParser.parse_binance_txt(request.data)
        missing_currencies = []
        added = []
        for element in parsed:
            try:
                currency = Currency.objects.get(
                    symbol=element['symbol'].upper())
            except Currency.DoesNotExist:
                missing_currencies.append(element['symbol'])
                continue

            try:
                PortfolioAsset.objects.get(
                    exchange=exchange, currency=currency, portfolio=portfolio, amount=element['amount'], status="LOCK")
            except PortfolioAsset.DoesNotExist:
                asset = PortfolioAsset.objects.create(currency=currency, portfolio=portfolio, amount=float(
                    element['amount']), apr=element['apr'], status="LOCK",  exchange=exchange, source="BATCH")
                asset.save()
                added.append(str(asset))

        return Response({'exchange': exchange.name, 'portfolio': portfolio.name, 'parsed': parsed, 'added': added, 'unknown currencies': missing_currencies})
