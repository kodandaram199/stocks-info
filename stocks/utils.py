import urllib2
from bs4 import BeautifulSoup
import json
from constants import STOCKS_DATA_KEYS

def convert_data_to_json(data):
    transformed_data = []
    for row in data:
        transformed_row = {}
        for index, value in enumerate(row):
            transformed_row[STOCKS_DATA_KEYS[index]] = value;
        transformed_data.append(transformed_row)
    return transformed_data

def crawl_and_scrap(url):
    data = {}
    req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0"})
    con = urllib2.urlopen( req )
    soup = BeautifulSoup(con.read().decode('utf-8'), 'html.parser', from_encoding="utf-8")
    div = soup.find('div', attrs={'id': 'stockSelectorData'})
    table = div.find('table')
    thead = div.find_all('th')
    tbody = div.find('tbody')
    tbody = tbody.find_all('tr')
    headings = [th.text.strip().encode('utf-8') for th in thead]
    headings.append('Near value')
    headings.append('Margin')
    fifty2WeekRangeIndex = headings.index('52-Week Price Range');
    priceIndex = headings.index('Pricemmm dd, hh:mm')
    rowsData = []
    for tr in tbody:
        cols = tr.find_all('td')
        cols = [td.text.strip() for td in cols]
        fifty2WeekRange = cols[fifty2WeekRangeIndex]
        [low, high] = fifty2WeekRange.split(' - ')
        low = low.split(',')
        low = ''.join(low)
        low = float(low)
        high = high.split(',')
        high = ''.join(high)
        high = float(high)
        priceWithDate = cols[priceIndex]
        dotIndex = priceWithDate.index('.')
        price = priceWithDate[0: dotIndex+3].split(',')
        price = ''.join(price)
        price = float(price)
        highDiff = high - price
        lowDiff = price - low
        # can use mean or median to check margin
        if lowDiff < highDiff:
            cols.append('Near to 52 Week Low at '+str(low))
            cols.append(str(lowDiff))
            cols.append('Y')
        elif highDiff < lowDiff:
            cols.append('Near to 52 Week High at '+str(high))
            cols.append(str(highDiff))
            cols.append('N')
        else:
            cols.append('Neutral')
            cols.append(str(0))
            cols.append('N')
        cols = [col.encode('utf-8') for col in cols]
        cols.append(round(low/price, 2))
        rowsData.append(cols)
    rowsData = convert_data_to_json(rowsData)
    data['headings'] = headings
    data['data'] = rowsData
    return data


