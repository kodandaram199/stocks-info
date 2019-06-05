import urllib2
from bs4 import BeautifulSoup
import json
from stocks.utils import convert_data_to_json, crawl_and_scrap

def get_nifty_data(urls):
    niftyData = []
    for url in urls:
        data = crawl_and_scrap(url)
        niftyData.append(data)
    return niftyData