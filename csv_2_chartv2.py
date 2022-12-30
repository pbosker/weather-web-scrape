import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pdf2image import convert_from_path
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts


def generate_chart():
    weatherStats = pd.read_csv('weather_scrape.csv')
    plt.plot(weatherStats.datetime, weatherStats.temperature,label = 'temperature')
    plt.plot(weatherStats.datetime, weatherStats.wind,label = 'wind')
    plt.plot(weatherStats.datetime, weatherStats.humidity,label = 'humidity')
    plt.suptitle('Weather History')
    plt.title('Dorr Michigan', fontdict={'fontsize':15,'fontweight':'bold'})
    plt.xlabel('Date')
    plt.ylabel('Units')
    plt.legend()
    plt.savefig('CSV_Weather_Visual.pdf')

def convert_chart_to_JPG():
    images = convert_from_path('/home/paul/python/CSV_Weather_Visual.pdf')
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')


def transfer_chart_to_WP():
    client = Client('https://paulbosker.com/xmlrpc.php', 'paul', 'Bd0E pWaM sImJ OXoj DrlI QwGn')

    filename = '/home/paul/python/page0.jpg'
    data = {
            'name': 'picture.jpg',
            'type': 'image/jpeg',  # mimetype
        }
    with open(filename, 'rb') as img:
        data['bits'] = xmlrpc_client.Binary(img.read())

    response = client.call(media.UploadFile(data))
    attachment_id = response['id']


generate_chart()
convert_chart_to_JPG()
transfer_chart_to_WP()
