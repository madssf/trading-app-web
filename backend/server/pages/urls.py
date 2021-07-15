from django.urls import path
from .views import *

pages_urls = [
    path('api/v1/my_portfolios/<int:id>',
         MyPortfolioID.as_view(), name='portfolioid'),
    path('api/v1/positions/batch_post/<int:portfolio_id>/<int:exchange_id>',
         BatchAddPositonsView.as_view(), name='batch_add_positions')
]
