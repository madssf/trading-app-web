from .parsers import PositionBatchParser
from django.shortcuts import render
from apps.portfolios.models import Portfolio, PortfolioAsset, PortfolioPosition
from apps.currencies.models import Currency
from apps.exchanges.models import Exchange
from django.http.response import JsonResponse
from rest_framework import mixins, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class MyPortfolioID(mixins.ListModelMixin, generics.GenericAPIView):

    def get(self, request, id):
        portfolio = Portfolio.objects.get(
            id=id, owner=request.user)

        return JsonResponse(portfolio.get_frontend_detail_data(), safe=False)


class BatchAddPositonsView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, portfolio_id, exchange_id, format=None):

        try:
            portfolio = Portfolio.objects.get(
                id=portfolio_id, owner=request.user)
        except Portfolio.DoesNotExist:
            return Response({'message': 'unknown portfolio'})
        try:
            exchange = Exchange.objects.get(id=exchange_id)
        except Exchange.DoesNotExist:
            return Response({'message': 'unknown exchange'})
        parsed = PositionBatchParser.parse_binance_txt(request.data)
        missing_currencies = []
        added = []
        for element in parsed:
            try:
                currency = Currency.objects.get(
                    symbol=element['symbol'].upper())
            except Currency.DoesNotExist:
                missing_currencies.append(element['symbol'])
            # get/create asset
            try:
                asset = PortfolioAsset.objects.get(
                    portfolio=portfolio, currency=currency)
            except PortfolioAsset.DoesNotExist:
                asset = PortfolioAsset.objects.create(
                    portfolio=portfolio, currency=currency)
                asset.save()
            try:
                PortfolioPosition.objects.get(
                    exchange=exchange, asset=asset, amount=float(element['amount']), status="LOCK", stake_end=element['stake_end'], stake_start=element['stake_start'], source="BATCH")
            except PortfolioPosition.DoesNotExist:
                # creating position

                position = PortfolioPosition.objects.create(
                    asset=asset, exchange=exchange, amount=float(element['amount']), status="LOCK", stake_end=element['stake_end'], stake_start=element['stake_start'], source="BATCH")
                position.save()
                added.append(str(position))

        return Response({'exchange': exchange.name, 'portfolio': portfolio.name, 'parsed': parsed, 'added': added, 'unknown currencies': missing_currencies})


