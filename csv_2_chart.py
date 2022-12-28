import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

str_filename = 'weather_scrape.csv'

fh = open(str_filename)
csv_reader = csv.reader(fh)

csv_header = next(csv_reader)
print(csv_header)

#df_sig = pd.read_csv(str_filename, parse_dates=['datetime'], header=None, skiprows=5, names=csv_header)
#df_sig = pd.read_csv(str_filename, parse_dates=['datetime'], index_col="datetime", header=None, skiprows=5, names=csv_header)
df_sig = pd.read_csv(str_filename, parse_dates=['datetime'], index_col="datetime")
#df.plot()

# find the optimum size of the chart
numbr = len(df_sig)
ht = max(df_sig['temperature'])
hh = max(df_sig['humidity'])
hw = max(df_sig['wind'])
mt = min(df_sig['temperature'])
mh = min(df_sig['humidity'])
mw = min(df_sig['wind'])
highest = max(ht, hh, hw)
lowest = min(mt, mh, mw)

print(df_sig)
plt.xlabel('Date')
plt.ylabel('Units')
plt.title('Weather History')
plt.xlim([0, numbr])
plt.ylim([lowest-5, highest+5])

#-------   TEMPERATURE   ------#
df_sig.temperature.plot()
plt.grid()
figure = plt.gcf()

#---------    WIND    ---------#
df_sig.wind.plot()
plt.grid()
figure = plt.gcf()

#-------    HUMIDITY    -------#
df_sig.humidity.plot()
plt.grid()
figure = plt.gcf()

#------- Generate PDF   -------#
figure.set_size_inches(4*1.6, 4)
plt.savefig('CSV_Weather_Visualization.pdf')
