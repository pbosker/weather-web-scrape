import requests
from bs4 import BeautifulSoup

url = "https://www.marketwatch.com/investing/stock/"
codes=["SCS", "HOG", "AAPL", "MSFT", "GOOG", "BUNZ"]

for code in codes:
   result = requests.get(url + code)
   soup = BeautifulSoup(result.text, "html.parser")
   lists = soup.find_all('div',class_="intraday__data")

   for list in lists:
       num = list.find('h2', class_="intraday__price").text
       print(code + ":  " + num[3:-1])

#f = open("/home/paul/python/weather_scrape.csv", "a+")
#f.seek(0)
#data = f.read(40)
#f.write(str(outfl))
#f.write("\n")
#f.close()

