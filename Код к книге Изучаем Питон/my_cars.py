from car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

import car
my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

from car import Battery
battery1 = Battery(17)
battery1.describe_battery()
battery1.upgrade_battery()
battery1.get_range()
battery1.describe_battery()
battery1 = Battery(18)
battery1.describe_battery()
