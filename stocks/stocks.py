import requests
from bs4 import BeautifulSoup
import datetime

url = "https://www.marketwatch.com/investing/stock/"
codes=["SCS", "HOG", "AAPL", "MSFT", "GOOG", "AMZN", "WWW", "SPTN", "TSLA", "PLUG", "ARRY", "COMP", "AMGN", "IBM", "CAT", "MMM", "XOM", "ABBV"]
listx = ","

def find_num_of_symbols():
    number_of_symbols = len(codes)
    return number_of_symbols

def get_stock_name(c):
    result = requests.get(url + c)
    soup = BeautifulSoup(result.text, "html.parser")
    lists = soup.find_all('div',class_="element element--company")
    for list in lists:
        long_name = list.find('h1', class_="company__name").text
        return long_name

def get_stock_price(c):
    result = requests.get(url + c)
    soup = BeautifulSoup(result.text, "html.parser")
    lists = soup.find_all('div',class_="intraday__data")
    for list in lists:
        num = list.find('h2', class_="intraday__price").text
        return num[3:-1]

dn = datetime.datetime.now()
outfl = str(dn) + ", "
number_of_symbols = find_num_of_symbols()

for x in range(number_of_symbols):
    listx = listx + codes[x] + ", "

for name in codes:
    long_name = get_stock_name(name)
    price = get_stock_price(name)
    outfl = outfl + price + ", "

f = open("/home/paul/python/stocks/stock_prices.csv", "a+")
f.seek(0)
data = f.read(40)
f.write(str(listx))
f.write("\n")
f.write(str(outfl))
f.write("\n")
f.close()

