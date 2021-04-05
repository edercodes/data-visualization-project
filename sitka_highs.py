import csv

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'      ### open file, and assign to resulting file object to f
with open(filename) as f:
    reader = csv.reader(f)      ### call csv.reader, passes file as argument, and creates reader object associated with that file
    header_row = next(reader)        ### calling next once gets first line of the file, which contains headers

    # Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')     ### pass list of highs to to plot() and plot points in red

# Format plot.
ax.set_title("Daily high temperatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()