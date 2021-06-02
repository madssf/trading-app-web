from django.http.response import HttpResponse
from django.shortcuts import render
from apps.portfolios.models import Portfolio, PortfolioAsset, Credentials, PortfolioParameter
from apps.currencies.models import Currency

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
   # print(assets)
    context = {
        'name': portfolio['name'],
        "id": portfolio['id'],
        "assets": assets,
    }
    print(context)
    return render(request, "my_portfolio.html", context)
