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
    print(crypto_data)
    return render(request, "tracker/home.html", {'crypto_data': crypto_data})

def chart(request, coin_id):
    # Fetch historical data for the selected coin
    response = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart', params={
        'vs_currency': 'usd',
        'days': '7'  # Fetch data for the last 7 days
    })
    chart_data = response.json()

    # Extract timestamps and prices
    timestamps = [data_point[0] for data_point in chart_data['prices']]
    prices = [data_point[1] for data_point in chart_data['prices']]

    return render(request, 'tracker/chart.html', {
        'timestamps': timestamps,
        'prices': prices,
        'coin_id': coin_id
    })