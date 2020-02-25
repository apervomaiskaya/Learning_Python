class Car():
    #Простая модель автомобиля
    def __init__(self, make, model, year):
        #Активирует атрибуты описания автомобиля    
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        #Возвращает аккуратно отформатированное описание
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        #Выводит пробег машины в милях
        print('Эта машина движется со скоростью ' + str(self.odometer_reading) 
        + ' км/ч')
        
    def update_odometer(self, mileage):
        #Устанавливает заданное значение на одометре
        #При попытке обратной подкрутки изменение отклоняется
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Вы не можете откручивать одометр!')
            
    def increment_odometer(self, miles):
        #Увеличивает показания одометра с заданным приращением
        self.odometer_reading += miles
        
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#my_new_car.odometer_reading = 23
my_new_car.update_odometer(23)
my_new_car.read_odometer()

print()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        #self.reading_number_served = 0
        
    def describe_restaurant(self):
        print('Ресторан ' + self.restaurant_name.title() + ' - ' + 
        self.cuisine_type + ' кухня')
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + ' открылся!')
        
    def read_number(self):
        print('Ресторан вмещает: ' + str(self.number_served) + ' человек')
        
    def set_number_served(self, number):
        #Устанавливает количество обслуженных посетителей
        self.number_served = number
        
    def increment_number_served(self, people_number):
        self.number_served += people_number
        
res = Restaurant('охота', 'грузинская', 170)

res.set_number_served(18)

print(res.cuisine_type.title() + ' кухня' + ' Вместительность ' + 
str(res.number_served) + ' человек')

res.describe_restaurant()

res.read_number()

res.increment_number_served(5)
res.read_number()

class User:
    def __init__(self, first_name, last_name, age, login, e_mail, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login = login
        self.e_mail = e_mail
        self.login_attempts = login_attempts
        
    def describe_user(self):
        print('Фамилия: ' + self.first_name.title() + ' Имя: ' + self.last_name.
        title() + ' Возраст: ' + self.age + ' Логин: ' + self.login + ' E_mail: ' 
        + self.e_mail)
        
    def greet_user(self):
        print('Привет, ' + self.last_name.title() + '!')
        
    def read_login_attempts(self):
        print('Количество попыток: ' + str(self.login_attempts))
        
    def set_login_numbers(self, login):
        self.login_attempts = login
    
    def increment_login_attempts(self, login):
        self.login_attempts += login
        
    def reset_login_attempts(self, login_attempts):
        self.login_attempts = 0
        print('Попытки обнулились')

user1 = User('Кривобоков', 'Олег', '36', 'onxu', 'onxu@ya.ru', 5)

print(user1.first_name)
user1.describe_user()
user1.greet_user()

print()

user1.increment_login_attempts(1)
user1.read_login_attempts()
user1.increment_login_attempts(1)
user1.read_login_attempts()
user1.reset_login_attempts(1)
user1.read_login_attempts()

print()

user1.increment_login_attempts(1)
user1.read_login_attempts()

print()

user1.reset_login_attempts(1)
user1.read_login_attempts()

print()







