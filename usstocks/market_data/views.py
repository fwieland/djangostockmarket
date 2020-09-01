from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm


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
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Has Been Added"))
            return redirect("add_stock")
    else:
        stock_quote = Stock.objects.all()
        output = []
        for stock_quote_item in stock_quote:
            api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + str(stock_quote_item) + "/quote?token=pk_cd665dda2a6d453f90863dd2e47a45fc")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Ticker Name Error..."
        return render(request, 'add_stock.html', {'stock_quote': stock_quote, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock Has Been Deleted"))
    return redirect(add_stock)