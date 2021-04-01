import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Title and label axes.
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubes of Value", fontsize=14)

# Tick label size.
ax.tick_params(axis='both', which='major', labelsize=14)

# Range of each axis.
ax.axis([0, 5500, 0, 5500000])

plt.savefig('cubes_plot.png', bbox_inches='tight')