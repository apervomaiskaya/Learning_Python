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
die1.roll_die(24)

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'а', 'б', 'в', 'г', 'д']
from random import choice

for i1 in lottery:
    i1 = choice(lottery)
for i2 in lottery:
    i2 = choice(lottery)
for i3 in lottery:
    i3 = choice(lottery)
for i4 in lottery:
    i4 = choice(lottery)
for i5 in lottery:
    i5 = choice(lottery)

print('Билет, содержащий эту комбинацию из цифр и букв, является выигрышным:', [i1, i2, i3, i4, i5])
x = [i1, i2, i3, i4, i5]
my_ticket = ['', 5, 'б', 9, 'д']

# for x in lottery:
#     if x not in my_ticket:
#         print('Комбинация', i1, i2, i3, i4, i5, 'не выиграла.')
#     else:
#         print('Комбинация', my_ticket, 'выиграла!')

for a in x:
    if a not in my_ticket:
        print('Комбинация', i1, i2, i3, i4, i5, 'не выиграла.')
    if a in my_ticket:
        print('Комбинация', my_ticket, 'выиграла!')









































