# НАЧАЛ ИЗУЧАТЬ КЛАССЫ 02 АПР. 2020 Г.

# class Cat():
#     # Простая модель собаки
#     def __init__(self, name, age):
#         # Инициализирует атрибуты name и age
#         self.name = name
#         self.age = age
#
#     def caress(self):
#         print(self.name.title(), 'теперь ластится!')
#
#     def purr(self):
#         print(self.name.title(), 'теперь мурчит!')
#
# my_cat = Cat('буся', 9)
# print('Мою кошку зовут', my_cat.name.title() + '.')
# print('Моей кошке', my_cat.age, 'лет.')
# # print(my_cat.name)
#
# my_cat.caress()
# my_cat.purr()
#
# print()
#
# your_cat = Cat('люси', 10)
# print('Твою кошку зовут', your_cat.name.title() + '.')
# print('Твоей кошке', your_cat.age, 'лет.')
# your_cat.caress()
# your_cat.purr()
#
# print()

# class Restaurant():
#     def __init__(self,  restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print('Этот ресторан называется', self.restaurant_name + '.')
#         print('Этот ресторан', self.cuisine_type, 'кухни.')
#
#     def open_restaurant(self):
#         print('Ресторан', self.restaurant_name, 'открыт!')
#
# restaurant = Restaurant('Пафос', 'русская')
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
#
# restaurant = Restaurant('Пафос', 'русская')
# restaurant.describe_restaurant()
# restaurant = Restaurant('Узбек Плюс', 'узбекская')
# restaurant.describe_restaurant()
# restaurant = Restaurant('Грузинский парень', 'грузинская')
# restaurant.describe_restaurant()

class User():
    def __init__(self, first_name, last_name, age, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.role = role

    def describe_user(self):
        print('\nМеня зовут', self.first_name.title(), self.last_name.title() + '.')
        print('Мне' , self.age , 'лет. Моя роль в проекте - ', self.role + '.')

    def greet_user(self):
        print('Здравствуйте,', self.first_name.title(), self.last_name.title() + '!')

user1 = User('олег', 'кривобоков', '36', 'админ')
user1.describe_user()
user1.greet_user()

user2 = User('саша', 'кривобокова', '36', 'пользователь')
user2.describe_user()
user2.greet_user()

user3 = User('ваня', 'одариченко', '30', 'пользователь')
user3.describe_user()
user3.greet_user()

print()

class Car():
#Простая модель автомобиля."""
    def __init__(self, make, model, year):
    #Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
    #Возвращает аккуратно отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
    #Выводит пробег машины в милях
        print('Эта машина разгоняется до', self.odometer_reading, 'миль/час')

    def update_odometer(self, mileage):
        # Устанавливает на одометре заданное значение.
        # При попытке обратной подкрутки изменение отклоняется.
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Вы не можете откручивать одометр назад!')

    def increment_odometer(self, miles):
        #Увеличивает показания одометра с заданным приращением."""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(101)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(2350)
my_used_car.read_odometer()
my_used_car.increment_odometer(10)
my_used_car.read_odometer()

class Restaurant():
    def __init__(self,  restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('Этот ресторан называется', self.restaurant_name + '.')
        print('Этот ресторан', self.cuisine_type, 'кухни.')

    def open_restaurant(self):
        print('Ресторан', self.restaurant_name, 'открыт!')

    def read_number_served(self):
        print(self.restaurant_name, 'обслужил', self.number_served, 'посетителей.')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant('Пафос', 'русская')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant1 = Restaurant('Запад', 'американская')
restaurant1.read_number_served()
restaurant1.set_number_served(15)
restaurant1.read_number_served()
restaurant1.increment_number_served(80)
restaurant1.read_number_served()

print()

class User():
    def __init__(self, first_name, last_name, age, role, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.role = role
        self.login_attempts = int(login_attempts)

    def describe_user(self):
        print('\nМеня зовут', self.first_name.title(), self.last_name.title() + '.')
        print('Мне' , self.age , 'лет. Моя роль в проекте - ', self.role + '.')

    def greet_user(self):
        print('Здравствуйте,', self.first_name.title(), self.last_name.title() + '!')

    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Олег', 'Кривобоков', 36, 'админ', '15')
print(user1.first_name)
print(user1.last_name)
print(user1.age)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
user1.increment_login_attempts(1)
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print('This car can go about', range, 'miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
            print('Мощность батареи увеличена до 100%!')

class ElectricCar(Car):
    #Представляет аспекты машины, специфические для электромобилей.
    def __init__(self, make, model, year):
        """инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery_size = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print('This car has a', self.battery_size, 'kWh battery.')

    def fill_gas_tank(self):
        """У электромобилей нет бензобака."""
        print("У электромобилей нет бензобака!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['ваниль', 'клубника', 'банан']

    def show_list_flavors(self):
        print(self.flavors)

icecreamstand1 = IceCreamStand('sdf', 'xcio')
icecreamstand1.show_list_flavors()

class Admin(User):
    def __init__(self, first_name, last_name, age, role, login_attempts):
        super().__init__(first_name, last_name, age, role, login_attempts)
        self.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей']

    def show_privileges(self):
        print(self.privileges)

admin1 = Admin('sdf', 'lk;', '48', 'admin', 4)
admin1.show_privileges()

class Privileges(Admin):
    def __init__(self):
        self.privileges = ['разрешено банить пользователей', 'разрешено громко смеяться']

    def show_privileges(self):
        print(self.privileges)

privileges1 = Privileges()
privileges1.show_privileges()

admin2 = Admin('Углук', 'Тузлук', 48, 'admin', 4)
admin2.show_privileges()

electriccar1 = ElectricCar('yamaha', 'gt-19', 2018)
electriccar1.battery_size.describe_battery()
electriccar1.battery_size.upgrade_battery()
electriccar1.battery_size.describe_battery()
