import requests
from bs4 import BeautifulSoup

# this program is designed to extrat weather information from a website.    The website is specified below

url = "https://paulbosker.com/2022/08/21/weather/"

#initialize variables. 
outfl = ""
have_t = "N"
have_h = "N"

# The below variables must be initialized here because if the value cannot be determined from the website, the program terminates when the variable is attempted to be printed.    
# By declaring the variables here, this problem is eliminated
t = 0.00
w = 0.00
h = 0.00

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
lists = soup.find_all('div',class_="lws-widget-row")

# Get current date/time from website (d & dt)
dt = soup.find_all(class_="elementor-shortcode")[0]
for d in dt:
    pass

# Get temperature (t) and wind (w)
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
# Get humidity (h)
for list2 in lists:
    node = list2.find('div', class_="lws-widget-med-value")
    if node is not None:
        num = list2.find('div', class_="lws-widget-med-value").text
        if list2.find('div', class_="lws-widget-med-unit").text == "%":
            if have_h == "N":
                h = num
                have_h = "Y"

# build output format
outfl = str(d) + "," + str(t) + "," + str(w) + "," + str(h)

# write to file
f = open("/home/paul/python/weather_scrape.csv", "a+")
f.seek(0)
data = f.read(40)
f.write(str(outfl))
f.write("\n")
f.close()

