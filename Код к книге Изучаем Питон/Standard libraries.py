from random import randint
print(randint(1, 696))

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, sides):
        from random import randint
        print(randint(1, sides))

die1 = Die(6)
die1.roll_die(6)
die1.roll_die(10)
die1.roll_die(20)

