from random import choice   ### random decisions are made by storing moves in a list and using the choice() function, from random module
                            ### to decide which move to make each time a step is taken
class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):    ### default number of points is made
        """Initialize attributes of a walk."""

        self.num_points = num_points

        # All walks start at (0,0).     ### list is made for both values
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:     ### loop is set up to run until walk is filled with correct number of points

            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])       ### value is set for each direction, 1 for right, and -1 for left, same for y below
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance       ### length fo each step determined by multiplying direction of movement and dsitance chosen

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejects moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)