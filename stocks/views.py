# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import json
from views_utils.nifty import get_nifty_data
from views_utils.nifty_fifty import get_nifty_fifty_data


# Create your views here.

from django.http import HttpResponse

urlNifty50 = 'https://www.valueresearchonline.com/stocks/StockSelector/default.asp?index=5'
urlNiftyNext50 = 'https://www.valueresearchonline.com/stocks/stockselector/default.asp?index=63'
urlNiftyMidCap100 = 'https://www.valueresearchonline.com/stocks/stockselector/default.asp?index=91'
urlNiftySmallCap100 = 'https://www.valueresearchonline.com/stocks/StockSelector/default.asp?index=173'

def index(request):
    data = get_nifty_data([urlNifty50, urlNiftyNext50, urlNiftyMidCap100, urlNiftySmallCap100])
    return HttpResponse(json.dumps(data))

def nifty_fifty(request):
    data = get_nifty_fifty_data(urlNifty50)
    return HttpResponse(json.dumps(data))

def nifty_next_fifty(request):
    data = get_nifty_fifty_data(urlNiftyNext50)
    return HttpResponse(json.dumps(data))

def nifty_mid_cap(request):
    data = get_nifty_fifty_data(urlNiftyMidCap100)
    return HttpResponse(json.dumps(data))

def nifty_small_cap(request):
    data = get_nifty_fifty_data(urlNiftySmallCap100)
    return HttpResponse(json.dumps(data))
