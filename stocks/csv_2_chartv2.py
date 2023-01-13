import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pdf2image import convert_from_path
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts


def generate_chart():
    weatherStats = pd.read_csv('stock_prices.csv')
    # DXCM,GILD,ROST,PDD,HON,AVGO,KLAC,KHC,BKNG,PCAR,NDAQ
    plt.plot(weatherStats.datetime, weatherStats.DXCM,label = 'DXCM')
    plt.plot(weatherStats.datetime, weatherStats.GILD,label = 'GILD')
    plt.plot(weatherStats.datetime, weatherStats.ROST,label = 'ROST')
    plt.plot(weatherStats.datetime, weatherStats.PDD,label = 'PDD')
    plt.plot(weatherStats.datetime, weatherStats.HON,label = 'HON')
    plt.plot(weatherStats.datetime, weatherStats.AVGO,label = 'AVGO')
    plt.plot(weatherStats.datetime, weatherStats.KLAC,label = 'KLAC')
    plt.plot(weatherStats.datetime, weatherStats.KHC,label = 'KHC')
    plt.plot(weatherStats.datetime, weatherStats.BKNG,label = 'BKNG')
    plt.plot(weatherStats.datetime, weatherStats.PCAR,label = 'PCAR')
    plt.plot(weatherStats.datetime, weatherStats.NDAQ,label = 'NDAQ')
    plt.suptitle('Top 10 Stock History')
    plt.title('My Picks', fontdict={'fontsize':15,'fontweight':'bold'})
    plt.xlabel('Date')
    plt.ylabel('Price per Share')
    plt.legend()
    plt.savefig('top10_stock_visual.pdf')

def convert_chart_to_JPG():
    images = convert_from_path('/home/paul/python/stocks/top10_stock_visual.pdf')
    for i in range(len(images)):
        # Save pages as images in the pdf
        images[i].save('stocks'+ str(i) +'.jpg', 'JPEG')


def transfer_chart_to_WP():
    client = Client('https://paulbosker.com/xmlrpc.php', 'paul', 'Bd0E pWaM sImJ OXoj DrlI QwGn')

    filename = '/home/paul/python/stocks/stocks0.jpg'
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
