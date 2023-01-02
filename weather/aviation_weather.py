from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import EditPost
from wordpress_xmlrpc.methods import posts
import json
import requests
import base64
import lxml.etree as etree
from bs4 import BeautifulSoup

def write_to_file(outf):
    # write to file
    f = open("/home/paul/python/weather/aviation_weather.xml", "a+")
    f.seek(0)
    data = f.read(40)
    f.write(str(outf))
    f.write("\n")
    f.close()


def print_xml(r):
    bs = BeautifulSoup(open(r), 'xml')
    pretty_xml = bs.prettify()
    print(pretty_xml)



#    x = etree.parse(r)
#    print(etree.tostring(x, pretty_print=True))

if __name__ == '__main__':
    url = "https://aviation-weather-center.p.rapidapi.com/adds/dataserver_current/httpparam"
    querystring = {"datasource":"metars","stationString":"KGRR","startTime":"2022-12-31T16:48:35Z","endTime":"2022-12-31T18:48:35Z"}
    headers = {
        "X-RapidAPI-Key": "59cf99f2d8mshd1a719884ee4f3cp154303jsna5cde8628710",
        "X-RapidAPI-Host": "aviation-weather-center.p.rapidapi.com"
    }
    response1 = requests.request("GET", url, headers=headers, params=querystring)

    print(response1.text)
    write_to_file(response1.text)
    print_xml("/home/paul/python/weather/aviation_weather.xml")
