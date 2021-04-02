from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()       ### two instances of Die are created
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):        ### rolls die 1000 times and stores results in a list
    result = die_1.roll() + die_2.roll()        ### dice is rolled and sum is calculated of the two dice for each roll
    results.append(result)

# Analyze the results.
frequencies = []        ### an empty list frequencies is created to store the number of times each value is rolled
max_result = die_1.num_sides + die_2.num_sides       ### the sum of the largest number on both dice, which is stored in max_result
for value in range(2, max_result+1):        ### loop through possible values
    frequency = results.count(value)        ### counts the number of results for each value between 2 and max_result
    frequencies.append(frequency)       ### value is then appended to list above

# Visualize the results.
x_values = list(range(2, max_result+1))        ### creates a list that starts at 1 and ends at number of dies
data = [Bar(x=x_values, y=frequencies)]        ### represents a data set that will be formatted as a bar chart

x_axis_config = {'title': 'Result', 'dtick': 1}        ### dtick key controls spacing between tick marks on the x-axis
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',        ### layout class returns an object that specifies the layout and config as a whole
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

print(frequency)