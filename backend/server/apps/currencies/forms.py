# articles/forms.py
from django import forms

from .models import Currency


class CurrencyForm(forms.ModelForm):

    class Meta:
        model = Currency
        fields = ["name", "symbol", "last_price",
                  "mcap_total", "mcap_rank", "pct_change_24h"]
