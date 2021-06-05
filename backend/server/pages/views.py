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
        portfolio_id=id, close_time=None).values()
    assets = []
    for asset in asset_qs:
        currency = Currency.objects.get(id=asset['currency_id'])
        assets.append(
            {
                'symbol': currency.symbol,
                'name': currency.name,
                'status': asset['status'],
                'amount': asset['amount'],
                'apr': asset['apr'],
                'stake_start': asset['stake_start'],
                'stake_end': asset['stake_end'],
                'value': asset['amount']*currency.last_price
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
    context = {
        'name': portfolio.name,
        "id": portfolio.name,
        "assets": assets,
        "strategy": strategy_name,
        "parameters": parameters
    }
    return render(request, "my_portfolio.html", context)
