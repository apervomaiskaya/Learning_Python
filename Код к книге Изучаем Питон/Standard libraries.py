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

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'а', 'б', 'в', 'г', 'д']
from random import choice
rannum = choice(lottery)
print(str(rannum), str(rannum), str(rannum), str(rannum), str(rannum))
for i1 in lottery:
    i1 = choice(lottery)
for i2 in lottery:
    i2 = choice(lottery)
for i3 in lottery:
    i3 = choice(lottery)
for i4 in lottery:
    i4 = choice(lottery)
print([i1, i2, i3, i4])
































