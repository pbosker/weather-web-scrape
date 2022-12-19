import csv
import requests
from bs4 import BeautifulSoup
import datetime

with open("/home/paul/python/stocks/stock_prices.csv", newline='') as f:
  reader = csv.reader(f)
  for row in reader:
#    print(str(row))
    break

url = "https://www.marketwatch.com/investing/stock/"

def get_stock_price(c):
    result = requests.get(url + c)
    soup = BeautifulSoup(result.text, "html.parser")
    lists = soup.find_all('div',class_="intraday__data")
    for list in lists:
        num = list.find('h2', class_="intraday__price").text
        return num[3:-1]

dn = datetime.datetime.now()
outfl = str(dn) + ", "

for name in row:
    if (str(name) == '') or (str(name) == ' '):
        continue
    else:
        price = get_stock_price(name)
        outfl = outfl + str(price) + ", "

f = open("/home/paul/python/stocks/stock_prices.csv", "a+")
f.seek(0)
data = f.read(40)
f.write(str(outfl))
f.write("\n")
f.close()

