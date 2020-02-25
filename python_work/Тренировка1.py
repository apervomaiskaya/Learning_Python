#import sys
#def silly_age_joke():
#   print('Сколько вам лет?')
#   age = int(sys.stdin.readline())
#   if age >= 10 and age <= 13:
#       print('13 + 49 + 84 + 155 + 97: что получится? Головная боль!')
#   else:
#       print('Что-что?')
#silly_age_joke()

#def moon_weight(ves):
    #weight = 3
    #for week in range (1, 53):
        #weight = weight+ves
        #print('Неделя %s, Вес: %s' % (week, moon_weight))

#def moon_weight(weight, ves):
#   for week in range(1, 15):
#       weight = weight + (weight*ves)/100
#       print('Год %s, Вес в этом году: %s' % (week, weight))
#moon_weight(30, 0.25)

#import sys
#def moon_weight():
#    print('Введите ваш нынешний земной вес')
#    weight = int(sys.stdin.readline())
#    print('Введите ежегодный прирост вашего веса')
#    uv = int(sys.stdin.readline())
#   print('Введите количество лет')
#   let = int(sys.stdin.readline())
#    for week in range(1, let):
#        weight = weight + (weight*uv)/100
#        print('Неделя %s, Лунный вес: %s' % (week, weight))
#moon_weight()

class Things:
        pass
class Inanimate(Things):
        pass
class Animate(Things):
        pass
class Sidewalks(Inanimate):
        pass
class Animals(Animate):
        def breathe(self):
            print('дышит')
        def move(self):
            print('двигается')
class Mammals(Animals):
        def feed_young_with_milk(self):
            print('кормит детенышей молоком')
class Giraffes(Mammals):
        def eat_leaves_from_trees(self):
            print('ест листья')
 
reginald = Giraffes()
harold = Giraffes()
reginald.move()
#harold.eat_leaves_from_trees()
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("Я нашел еду!")
    def dance_a_jig(self):
        self.move()
        self.move()
reginald = Giraffes()
reginald.dance_a_jig()



class Things:
        pass
class Animate(Things):
        pass
class Animals(Animate):
        def left_foot_forward(self):
            print('левая нога впереди')
        def left_foot_back(self):
            print('левая нога сзади')
        def right_foot_forward(self):
            print('правая нога впереди')
        def right_foot_back(self):
            print('правая нога сзади')
class Mammals(Animals):
        pass
class Giraffes(Mammals):
    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()
reginald = Giraffes()
reginald.dance()


class Giraffes:
        def __init__(self, spots):
                self.giraffe_spots = spots 
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)

#import turtle
#avery = turtle.Pen()
#kate = turtle.Pen()
#avery.forward(50)
#avery.right(90)
#avery.forward(20)
#kate.left(90)
#kate.forward(100)
#jacob = turtle.Pen()
#jacob.left(180)
#jacob.forward(80)

class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    def breathe(self):
        print('дышит')
    def move(self):
        print('двигается')
    def eat_food(self):
        print('ест')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('кормит детенышей молоком')
    
class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('ест листья')
reginald = Giraffes()
harold = Giraffes()
class Giraffes(Mammals):
    def find_food(self):
        self.move()
        print("Я нашел еду!")
        self.eat_food()
    def dance_a_jig(self):
        self.move()
        self.move()
        self.move()
        self.move()
reginald = Giraffes()
reginald.dance_a_jig()
class Giraffes:
    def __init__(self, spots):
        self.giraffe_spots = spots
        
ozwald = Giraffes(100)
gertrude = Giraffes(150)
print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)


class Mammals:
    pass
class Giraffes(Mammals):
    def left(self):
        print('Левая')
    def dance(self):
        self.left()
regi = Giraffes()
regi.dance()

class Giraffes:
    def __init__(self, spots):
        self.giraffes_spots = spots
regi = Giraffes(100)
print(regi.giraffes_spots)

class Giraffes:
    def __init__(self, spots):
        self.giraffes_spots = spots
regi = Giraffes(173)
print(regi.giraffes_spots)

print(abs(-10))

steps = -3
if abs(steps) > 0:
    print('Персонаж двигается')

print (bool(0))

print(bool(-0.5))

print(bool('Как назвать свинью на соревнованиях по карате? Свиная отбивная!'))

my_silly_list = ['s', 'i', 'l', 'l', 'y']
print(bool(my_silly_list))

float('12')

float('123.456789')

#your_age = input('Введите ваш возраст: ')
#age = float(your_age)
#if age > 13:
#    print('Вы на %s лет старше, чем положено' % (age - 13))

print(len('это тестовая строка'))
creature_list = ['единорог', 'циклоп', 'фея', 'эльф', 'дракон', 'тролль']
print(len(creature_list))

enemies_map = {'Бэтмен' : 'Джокер',
'Супермен' : 'Лекс Лютор',
'Человек-паук' : 'Зеленый гоблин'}
print(len(enemies_map))

fruit = ['яблоко', 'банан', 'клементин', 'питайя']
length = len(fruit)
for x in range(0, length):
    print('фрукт с индексом %s: %s' % (x, fruit[x]))

numbers = [5, 4, 10, 30, 22]
print(max(numbers))

strings = 'строкаСТРОКА'
print(max(strings))

guess_this_number = 31
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
    print('Бабах! Вы проиграли')
else:
    print('Вы победили')

#import turtle
#avery = turtle.Pen()
#kate = turtle.Pen()
#jacob = turtle.Pen()
#ben = turtle.Pen()
#avery.forward(100)
#avery.left(90)
#avery.forward(50)
#avery.right(90)
#avery.forward(50)
#kate.forward(100)
#kate.right(90)
#kate.forward(50)
#kate.left(90)
#kate.forward(50)
#jacob.forward(110)
#jacob.left(90)
#jacob.forward(30)
#jacob.right(90)
#jacob.forward(20)
#ben.forward(110)
#ben.right(90)
#ben.forward(30)
#ben.left(90)
#ben.forward(20)

print(eval('10*5'))

for x in range(0, 5):
    print(x)
print(list(range(0, 5)))

count_by_twos = list(range(0, 30, 2))
print(count_by_twos)

count_down_by_twos = list(range(40, 10, -2))
print(count_down_by_twos)

my_list_of_numbers = list(range(0, 500, 50))
print(my_list_of_numbers)
print(sum(my_list_of_numbers))

#test_file = open ('E:\Другие загрузки\\test.txt')
#text = test_file.read()
#print(text)

#test_file = open('E:\Другие загрузки\\test.txt', 'w')
#test_file.write('Что это – зеленое и крякает? Жабокряк!')
#test_file.close()

#test_file = open ('E:\Другие загрузки\\test.txt')
#text = test_file.read()       
#test_file = open('E:\Другие загрузки\\test.txt', 'w')
#test_file.write('Товары для ландшафтного дизайна')
#test_file.close()


a = abs(10) + abs(-37)
print(a)

b = abs(-10) + -10
print(b)


class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
import copy
harry = Animal('гиппогриф', 6, 'розовый')
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)

harry = Animal('гиппогриф', 6, 'розовый')
carrie = Animal('химера', 4, 'в зеленый горошек')
billy = Animal('богл', 0, 'узорчатый')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)
my_animals[0].species = 'вампир'
print(my_animals[0].species)
print(more_animals[0].species)

sally = Animal('сфинкс', 4, 'песочный')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))

more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'дракон'
print(my_animals[0].species)
print(more_animals[0].species)

import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('ozwald'))
print(keyword.kwlist)

import random
print(random.randint(1, 100))
print(random.randint(100, 1000))
print(random.randint(1000, 5000))

#import random
#num = random.randint(1, 100)
#while True:
#   print('Угадайте число от 1 до 100')
#   guess = input()
#    i = int(guess)
#   if i == num:
#       print('Правильно!')
#        break
#    elif i < num:
#        print('Загаданное число больше')
#   elif i > num:
#       print('Загаданное число меньше')

import random
desserts = ['мороженое', 'блинчики', 'кекс', 'печенье', 'конфеты']
print(random.choice(desserts))

import random
desserts = ['мороженое', 'блинчики', 'пирог', 'печенье',
'конфеты']
random.shuffle(desserts)
print(desserts)

import sys
sys.stdout.write("У какого слона нет хобот? У шахматного!")

import sys
print(sys.version)

import time
print(time.time())

def lots_of_numbers(max):
    for x in range(0, max):
        print(x)
lots_of_numbers(10)
def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('Прошло %s секунд' % (t2-t1))

import time
print(time.asctime())
t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)

import time
t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))

for x in range(1, 21):
        print(x)
        time.sleep(0)

#import pickle
#game_data = {
#'позиция-игрока' : 'С23 В45',
#'карманы' : ['ключи', 'карманный нож', 'гладкий камень'],
#'рюкзак' : ['веревка', 'молоток', 'яблоко'],
#'деньги' : 158.50}
#save_file = open('save.txt', 'wb')
#pickle.dump(game_data, save_file)
#save_file.close()
#load_file = open('save.txt', 'rb')
#loaded_game_data = pickle.load(load_file)
#load_file.close()
#print(loaded_game_data)

import copy
class Car:
    pass
car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)
car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)

import sys
print(sys.version)

def lots_of_numbers(max):
        t1 = time.time()
        for x in range(0, max):
                print(x)
        t2 = time.time()
        print('Прошло %s секунд' % (t2-t1))
lots_of_numbers(10)

#import turtle
#t = turtle.Pen()
#t.reset()
#for x in range(1, 38):
#    t.forward(100)
#    t.left(175)

#import turtle
#t = turtle.Pen()
#t.reset()
#for x in range(1, 20):
#    t.forward(100)
#    t.left(95)

#import turtle
#t = turtle.Pen()
#t.reset()
#for x in range(1, 19):
#    t.forward(100)
#    if x % 2 == 0:
#        t.left(175)
#    else:
#        t.left(225)

#def hello():
#    print('привет')
#from tkinter import *
#tk = Tk()
#btn = Button(tk, text="нажми меня", command=hello)
#btn.pack()

def person(width, height):
    print('Моя ширина - %s, а высота - %s' % (width, height))
person(height=3, width=4)


class Person():
    def __init__(self, name):
        self.name = name
hunter = Person('Elmer Fudd')
print('The mighty hunter: ', hunter.name)

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name
        
class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"
        
person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

class Car():
    def exclaim(self):
        print("I'm a Car!")
class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")
give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()
#give_me_a_yugo.exclaim()

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius
c = Circle(5)
c.radius = 7
print(c.diameter)

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()



