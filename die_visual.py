from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die

# Create a D6.
die = Die()        ### an instance of Die with the default 6 sides is created

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):        ### rolls die 100 times and stores results in a list
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []        ### an empty list frequencies is created to store the number of times each value is rolled
for value in range(1, die.num_sides+1):        ### loop through possible values
    frequency = results.count(value)        ### counts how many times each number appears in results
    frequencies.append(frequency)       ### value is then appended to list above

# Visualize the results.
x_values = list(range(1, die.num_sides+1))        ### creates a list that starts at 1 and ends at number of dies
data = [Bar(x=x_values, y=frequencies)]        ### represents a data set that will be formatted as a bar chart

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',        ### layout class returns an object that specifies the layout and config as a whole
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

print(frequency)