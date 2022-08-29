from django.contrib import messages
from .forms import StockForm
import requests
import json
from django.shortcuts import redirect, render
from .models import StockClass


def home(request):

    # pk_7f4138c8aa56465b9fd1525a01b16583

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"+ticker+"/quote?token=pk_7f4138c8aa56465b9fd1525a01b16583")

        try:
            api = json.loads(api_request.content)
            
        except Exception as e:
            api = "Error..."
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "ticker sample"})


def about(request):

    return render(request, 'about.html', {})


def add_stock(request):
    if request.method == 'POST':
        
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock Added Succesfully!"))
            return redirect('add_stock')
    else:
        ticker = StockClass.objects.all()
        output = []
        ticker_symbols = []
        for ticker_item in ticker:
            api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/"+str(ticker_item)+"/quote?token=pk_7f4138c8aa56465b9fd1525a01b16583")

            try:
                api = json.loads(api_request.content)
                output.append(api)
                ticker_symbols.append(ticker_item)

            except Exception as e:
                api = "Error..."
           
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output, 'ticker_symbols': ticker_symbols })    
        


def delete(request, stock_id):
    item = StockClass.objects.get(pk = stock_id)
    item.delete()
    messages.success(request, ("Stock Deleted Succesfully!"))
    return redirect('add_stock')
