from django.shortcuts import render
from .models import Stock

def index(request):
    import requests
    import json

    if request.method == 'POST':
        ticker_name = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker_name + "/quote?token=pk_cd665dda2a6d453f90863dd2e47a45fc")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Ticker Name Error..."
        return render(request, 'index.html', {'api': api})
    else:
        return render(request, 'index.html', {'ticker': "Enter a ticker Symbol above.."})






def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    stock_quote = Stock.objects.all()
    return render(request, 'add_stock.html', {'stock_quote': stock_quote})