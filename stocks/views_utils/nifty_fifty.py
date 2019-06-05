from stocks.utils import convert_data_to_json, crawl_and_scrap

def get_nifty_fifty_data(url):
    data = crawl_and_scrap(url)
    return data