from sources import daily, weekly
print("Daily forecast:", daily.forecast())
print("Weekly forecast:")
for number, outlook in enumerate(weekly.forecast(), 1):
	print(number, outlook)
print('hello world')

import math
print(math.sqrt(9))
help(math)


