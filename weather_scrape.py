import requests
from bs4 import BeautifulSoup

url = "https://paulbosker.com/2022/08/21/weather/"
outfl = ""
have_t = "N"
have_h = "N"
have_p = "N"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
lists = soup.find_all('div',class_="lws-widget-row")
dt = soup.find_all(class_="elementor-shortcode")[0]
for d in dt:
    pass

for list1 in lists:
    node = list1.find('div', class_="lws-widget-big-value")
    if node is not None:
        num = list1.find('div', class_="lws-widget-big-value").text
        if list1.find('div', class_="lws-widget-big-unit").text == "°F":
            if have_t == "N":
                t = num
                have_t = "Y"
        elif list1.find('div', class_="lws-widget-big-unit").text == "mph":
            w = num
        elif list1.find('div', class_="lws-widget-big-unit").text == "in/h":
            r = num

for list2 in lists:
    node = list2.find('div', class_="lws-widget-med-value")
    if node is not None:
        num = list2.find('div', class_="lws-widget-med-value").text
        if list2.find('div', class_="lws-widget-med-unit").text == "%":
            if have_h == "N":
                h = num
                have_h = "Y"
        elif list2.find('div', class_="lws-widget-med-unit").text == "inHg":
            if have_p == "N":
                p = num
                have_p = "Y"
outfl = str(d) + "," + str(t) + "," + str(w) + "," + str(h) + "," + str(p) + "," + str(r)

f = open("/home/paul/python/weather_scrape.csv", "a+")
f.seek(0)
data = f.read(40)
f.write(str(outfl))
f.write("\n")
f.close()

