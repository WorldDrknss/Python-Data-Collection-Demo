import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    #print(header_row)

    #Enumerating Header
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    

    #Get High Temperatores
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
    
#Print to console
#print(highs)

#Lets plot the temperatores
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='black', alpha=0.1)

#Format Plot
ax.set_title("Daily Temperatures for 2018", fontsize=14)
ax.set_xlabel('Sitka Airport', fontsize=12)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=8)

plt.show()