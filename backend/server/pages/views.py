from django.http.response import HttpResponse
from django.shortcuts import render
from apps.portfolios.models import Portfolio, PortfolioAsset, Credentials, PortfolioParameter
from apps.currencies.models import Currency
from apps.strategies.models import Strategy, Parameter

from django.http import HttpResponse, JsonResponse
from django.core.serializers import json


def MyPortfoliosView(request):
    # create a dictionary
    portfolios = Portfolio.objects.filter(owner=request.user)
    context = {
        "data": portfolios,
    }
    # return response
    return render(request, "my_portfolios.html", context)


def PortfolioID(request, id):
    portfolio = Portfolio.objects.get(owner=request.user, id=id)

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
        currency_name = Currency.objects.get(symbol=currency).name
        assets.append(

            {
                'symbol': currency,  # ['name'],
                'name': currency_name,
                'total': round(sums['tot'], 2),
                'average': round(asset['average'], 2)

            }

        )
    params_qs = PortfolioParameter.objects.filter(
        portfolio=portfolio.id).values()
    parameters = []
    for param in params_qs:
        parameters.append({Parameter.objects.filter(
            id=param['parameter_id'])[0].name: param['value']})
       # parameters.append({Parameter.objects.filter().values()})
    try:
        strategy_name = Strategy.objects.get(id=portfolio.strategy.id).name
    except AttributeError as e:
        strategy_name = "No strategy"
    print(strategy_name)
   # print(assets)
    context = {
        'name': portfolio.name,
        "id": portfolio.name,
        "assets": assets,
        "strategy": strategy_name,
        "parameters": parameters
    }
    return render(request, "my_portfolio.html", context)
