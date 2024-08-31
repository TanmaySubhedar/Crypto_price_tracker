from django.shortcuts import render
import requests


def home(request):
    response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={
        'vs_currency': 'usd',
        'order': 'market_cap_desc',
        'per_page': 10,
        'page': 1,
        'sparkline': 'false'
    })
    crypto_data = response.json()
    return render(request, "tracker/home.html", {'crypto_data': crypto_data})
