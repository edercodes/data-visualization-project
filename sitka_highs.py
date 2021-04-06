import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'      ### open file, and assign to resulting file object to f
with open(filename) as f:
    reader = csv.reader(f)      ### call csv.reader, passes file as argument, and creates reader object associated with that file
    header_row = next(reader)        ### calling next once gets first line of the file, which contains headers

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []     ### two lists are created to attain values from file
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')        ### data containing date info converted to datetime object
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')     ### pass list of highs to to plot() and plot points in red
ax.plot(dates, lows, c='blue')

# Format plot.
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()     ### draws date labels diagaonolly to prevent them from overlapping
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()