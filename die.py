from random import randint

class Die:
    """A class representing a single line."""

    def __init__(self, num_sides=6):        ### argument is made for number of sides of the die
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):        ### this method uses the randint() function to return a random number between 1 and the number of sides
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)