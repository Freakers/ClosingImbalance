#!/usr/bin/env python
import urllib.request
import urllib.response
import pytz
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime
#from pandas.io.data import DataReader
import pandas_datareader as pdr

#SITE = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
SITE = "https://markets.businessinsider.com/index/components/s&p_500"
START = datetime(1900, 1, 1, 0, 0, 0, 0, pytz.utc)
END = datetime.today().utcnow()


def scrape_list(site):
    hdr = {'User-Agent': ''}
    page = urllib.request.urlopen(site)
    #page = urllib.open(req)
    soup = BeautifulSoup(page, "lxml")

    table = soup.find('table', {'class': 'table table-small'})
    tickers = dict()
    count = 1
    for row in table.findAll('tr'):
        col = row.findAll('td')
        name = col.findAll('a')
        ticker = str(name).rfind()
        if len(ticker) > 0:
            key = str("S&P500")
            tickers[count] = ticker
            count = count + 1
    print(tickers)
    return tickers


def download_ohlc(sector_tickers, start, end):
    sector_ohlc = {}
    for sector, tickers in sector_tickers.iteritems():
        print('Downloading data from Yahoo for %s sector' % sector)
        data = pdr(tickers, 'yahoo', start, end)
        for item in ['Open', 'High', 'Low']:
            data[item] = data[item] * data['Adj Close'] / data['Close']
        data.rename(items={'Open': 'open', 'High': 'high', 'Low': 'low',
                           'Adj Close': 'close', 'Volume': 'volume'},
                    inplace=True)
        data.drop(['Close'], inplace=True)
        sector_ohlc[sector] = data
    print('Finished downloading data')
    return sector_ohlc


def store_HDF5(sector_ohlc, path):
    with pd.get_store(path) as store:
        for sector, ohlc in sector_ohlc.iteritems():
            store[sector] = ohlc


def get_snp500():
    """

    :rtype: object
    """
    sector_tickers = scrape_list(SITE)
    sector_ohlc = download_ohlc(sector_tickers, START, END)
    store_HDF5(sector_ohlc, 'snp500.h5')


#if __name__ == '__main__':
#    get_snp500()

scrape_list(SITE)
