import bs4 as bs
import pickle
import requests

def save_sp500_tickers():
    headers = {'User-Agent': ''}
    resp = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies/", headers)
    soup = bs.BeautifulSoup(resp.text, "lxml")
    table = soup.find('table', {'class' : 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr'):
        tickers = row.findAll('td')[1].texrt()
        tickers.append(tickers)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers









