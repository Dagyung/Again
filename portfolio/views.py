from django.shortcuts import render
from .models import Portfolio #models.py의 함수와 동일하게!

def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'porfol.html', {'portfolios':portfolios})



