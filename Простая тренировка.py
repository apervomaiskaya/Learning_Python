# countries = ['Канада', 'Великобритания', 'США', 'Италия', 'Мальта', 'Япония']
# print(countries)
# print(sorted(countries))
# print(countries)
# print(sorted(countries))
# countries.sort(reverse = True)
# print(countries)
# countries.sort(reverse = False)
# print(countries)
# countries.sort()
# print(countries)
# list_of_guest = ['Стивен Хокинг', 'Сергей Доренко', 'Кирилл Рогов']
# print(len(list_of_guest))
# print(list_of_guest[-0])

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
# 	print(f"{magician.title()}, that was a great trick!")
# 	print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")

# print()

# list_of_pizza = ['колбасная', 'сырная', 'огуречная']

# for pizza in list_of_pizza:
# 	print('Я люблю', pizza, 'пиццу.')

# print('\nЯ действительно люблю пиццу!')

# for value in range(6):
# 	print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# квадраты = []
# for squre in range(1, 11):
# 	квадраты.append(squre**2)
# print(квадраты)

# squares = [square**2 for square in range(1, 11)]
# print(squares)

# for i in range(1, 21):
# 	print(i)

# # for i in range(1, 1000001):
# # 	print(i)

# million = [value for value in range(1, 1000001)]
# print(million)
# print(max(million))
# print(min(million))
# print(sum(million))

# for i in range(1, 20, 1):
# 	print(i)

# for i in range (3, 31, 3):
# 	print(i)

# list_3 = [i for i in range(3, 31, 3)]
# print(list_3) 

# a = []
# for i in range(1, 11):
# #	i = i**3
# 	a.append(i**3)
# print(a)

# a = [i**3 for i in range(1, 11)]
# print(a)

# print(million[0:50000])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[2:])
# print(players[0:4:2])

# my_foods = ['pizza', 'falafel', 'carrot cake', 'пельмени', 'блины']
# friend_foods = my_foods[:]

# my_foods.append('мясной САЛАТ')
# friend_foods.append('овощной салат')

# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# print('The irst three items in the list are:', my_foods[0:4])
# print('Three items from the middle of the list are:', my_foods[1:4])
# print('The last three items in the list are:', my_foods[-3:])
# print(my_foods)

# my_pizzas = ['pizza', 'falafel', 'carrot cake', 'пельмени', 'блины']
# friend_pizzas = my_foods[:]
# my_pizzas.append('ванильная')
# friend_pizzas.append('сахарная')
# for pizza in my_pizzas:
# 	print('My favorite pizzas are:', pizza)

# for pizza in friend_pizzas:
# 	print('My friend’s  favorite pizzas are:', pizza)


# # million = [value for value in range(1, 1000001)]
# # print(million)
# a = [pizza for pizza in my_pizzas]
# print(a)
# a = [pizza for pizza in friend_pizzas]
# print(a)

# dims1 = ('один', 'два','три', 'четыре','пять', 'шесть')
# print(dims1[0])
# print(dims1[1])
# for i in dims1:
# 	print(i)

# dims2 = ('два1', 'три1','три', 'четыре','пять', 'шесть')
# for i in dims2:
# 	print(i)

# cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
# 	if car == 'bmw':
# 		print(car.upper())
# 	else:
# 		print(car.title())

# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':
# 	print("Hold the anchovies!")

# age_0 = 22
# age_1 = 22
# age_0 >= 21 and age_1 >= 21
# (age_0 >= 21) and (age_1 >= 21)
# age_0 = 18
# age_0 >= 21 or age_1 >= 21

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# 'mushrooms' in requested_toppings

# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banned_users:
# 	print(f"{user.title()}, you can post a response if you wish.")

# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# car = 'bmw'
# print("Is car == 'subaru'? I predict False.")
# print(car == 'subaru')

# car = 'audi'
# print("Is car == 'subaru'? I predict False.")
# print(car == 'subaru')

# car = 'mercedes'
# print("Is car == 'mercedes'? I predict True.")
# print(car == 'mercedes')

# car = 'honda'
# print("Is car == 'honda'? I predict True.")
# print(car == 'honda')

# print()

# car = 'subaru'
# print(car == 'subaru')
# print(car == 'honda')

# banned_users = ['andrew', 'carolina', 'david']
# new_users = ['oleg']
# for user in new_users:
# 	user = user.lower() 
# if user in banned_users:
# 	print('Вы забанены')
# else:
# 	print('Вы НЕ забанены')

# age = 17
# if age >= 18:
# 	print("You are old enough to vote!")
# 	print("Have you registered to vote yet?")
# else:
# 	print("Sorry, you are too young to vote.")
# 	print("Please register to vote as soon as you turn 18!")

# age = 64
# price = 40
# if age < 4:
# 	price = 0
# elif age < 18:
# 	price = 25
# elif age < 65:
# 	price 
# elif age >= 65:
# 	price = price/2
# print(f"Your admission cost is ${price}.")

# print()

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
# 	print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
# 	print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
# 	print("Adding extra cheese.")
# print("\nFinished making your pizza!")

# print()

# alien_color = 'red'
# if alien_color == 'green':
# 	print('Вы только заработали 5 очков!')
# elif alien_color == 'yellow':
# 	print('Вы только что заработали 10 очков!')
# elif alien_color == 'red':
# 	print('Вы только что заработали 15 очков!')

# alien_color = 'green'
# if alien_color == 'green':
# 	print('Вы только заработали 5 очков!')
# elif alien_color == 'yellow':
# 	print('Вы только что заработали 10 очков!')
# elif alien_color == 'red':
# 	print('Вы только что заработали 15 очков!')

# alien_color = 'yellow'
# if alien_color == 'green':
# 	print('Вы только заработали 5 очков!')
# elif alien_color == 'yellow':
# 	print('Вы только что заработали 10 очков!')
# elif alien_color == 'red':
# 	print('Вы только что заработали 15 очков!')

# print()

# age = 35
# if age < 2:
# 	print('Вы младенец!')
# elif (age >= 2) and (age < 4):
# 	print('Вы малыш!')	
# elif (age >= 4) and (age < 13):
# 	print('Вы ребёнок!')
# elif (age >= 13) and (age < 20):
# 	print('Вы подросток!')
# elif (age >= 20) and (age < 65):
# 	print('Вы взрослый!')
# elif age >= 65:
# 	print('Вы пожилой человек!')

# print()

# favorite_fruits = ['бананы', 'дыня', 'манго']
# if 'бананы' in favorite_fruits:
# 	print('Вы действительно любите бананы!')
# if 'арбуз' in favorite_fruits:
# 	print('Вы действительно любите арбуз!')
# if 'дыня' in favorite_fruits:
# 	print('Вы действительно любите дыню!')
# if 'виноград' in favorite_fruits:
# 	print('Вы действительно любите виноград!')
# if 'манго' in favorite_fruits:
# 	print('Вы действительно любите манго!')

# print()

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
# 	if requested_topping == 'green peppers':
# 		print("Sorry, we are out of green peppers right now.")
# 	else:
# 		print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# requested_toppings = []
# if requested_toppings:
# 	for requested_topping in requested_toppings:
# 		print(f"Adding {requested_topping}.")
# 		print("\nFinished making your pizza!")
# 	else:
# 		print("Are you sure you want a plain pizza?")

# available_toppings = ['mushrooms', 'olives', 'green peppers',
# 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
# 	if requested_topping in available_toppings:
# 		print(f"Adding {requested_topping}.")
# 	else:
# 		print(f"Sorry, we don't have {requested_topping}.")
# print("\nFinished making your pizza!")

# print()

# available_users = []
# if available_users:
# 	for available_user in available_users:
# 		if available_user == 'admin':
# 			print('Hello', available_user, 'would you like to see a status report?')
# 		else:
# 			print('Hello', available_user, 'thank you for logging in again.')
# else:
# 	print('We need to find some users!')

# print()

# current_users = ['mushrooms', 'olives', 'green peppers',
# 				'pepperoni', 'pineapple', 'extra cheese', 'admin']

# new_users = ['oleg', 'Olives', 'vanya',
# 			'sasha', 'tanaya', 'busya', 'Admin']

# for new_user in new_users:
# 	new_user = new_user.lower()
# 	#current_users = []
# 	if new_user in current_users:
# 		print(new_user, 'Вы должны выбрать новое имя!')
# 	else:
# 		print(new_user, 'Имя свободно!')

# print()

# por_chisl = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in por_chisl:
# 	if str(i) == '1':
# 		print(str(i) + 'st')
# 	elif str(i) == '2':
# 		print(str(i) + 'nd')
# 	elif str(i) == '3':
# 		print(str(i) + 'rd')
# 	else:
# print(str(i) + 'th')

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")
# # Пришелец перемещается вправо.
# # Вычисляем величину смещения на основании текущей скорости.

# alien_0['speed'] = 'fast'

# if alien_0['speed'] == 'slow':
# 	x_increment = 1
# elif alien_0['speed'] == 'medium':
# 	x_increment = 2
# else:
# 	# Пришелец двигается быстро.
# 	x_increment = 3
# # Новая позиция равна сумме старой позиции и приращения.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# favorite_languages = {
# 	'jen': 'python',
# 	'sarah': 'c',
# 	'edward': 'ruby',
# 	'phil': 'python',
# 	}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")
# print(favorite_languages['sarah'])

# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# Сергей_Доренко = {'first_name':'Сергей', 'last_name':'Доренко', 
# 				'age':'67', 'city':'Москва',}

# print(Сергей_Доренко['first_name'])
# print(Сергей_Доренко['last_name'])
# print(Сергей_Доренко['age'])
# print(Сергей_Доренко['city'])

# list_of_fav_digits = {'oleg':'15', 
# 					  'sasha':'47', 
# 					  'vanya':'645', 
# 					  'tanya':'54', 
# 					  'tanya':'78'
# 					  ,}

# print('Любимое число Олега:', list_of_fav_digits['oleg'])
# print('Любимое число Саши:', list_of_fav_digits['sasha'])
# print('Любимое число Вани:', list_of_fav_digits['vanya'])
# print('Любимое число Тани:', list_of_fav_digits['tanya'])
# print('Любимое число Лёши:', list_of_fav_digits['tanya'])

# print()


# list_of_definitions = {'список':'тип данных, который хранит набор или последовательность элементов.', 
# 					  'кортеж':'последовательность элементов, которая является неизменяемым типом. \rПоэтому мы не можем добавлять или удалять элементы в кортеже, изменять его.', 
# 					  'vanya':'645', 
# 					  'tanya':'54', 
# 					  'tanya':'78',
# 					  'vanya':'55'}

# print('\nСписок - это ', list_of_definitions['список'])
# print('\nКортеж - это ', list_of_definitions['кортеж'])

# print()

# for key, value in list_of_fav_digits.items():
# 	print(key, value)

# print()

# for key in list_of_fav_digits.keys():
# 	print(key)

# print()

# for value in set(list_of_fav_digits.values()):
# 	print(value)

# print()

# for name, digit in list_of_fav_digits.items():
# 	print(f"{name.title()}'s favorite digit is {digit.title()}.")

# print()

# if 'andrey' not in list_of_fav_digits:
# 	print('Андрей, прими, пж, участие в опросе!')

# print()

# for name in sorted(list_of_fav_digits.keys()):
# 	print(name.title() + ', спасибо за участие в опросе!')

# print()

# for i in set(list_of_definitions.keys()):
# 	print(i)

# print()

# list_of_voters = {'oleg', 'andrey', 'olya', 'sasha', 'don diablo'}

# already_voted = {'oleg':'python', 
# 				'sasha':'C', 
# 				'vanya':'C++', 
# 				'tanya':'Ryby', 
# 				'tanya':'Scala'
# 				,}

# for i in list_of_voters:
# 	if i in already_voted:
# 		print(i + ', спасибо за опрос!')
# 	else:
# 		print(i + ', пожалуйста, проголосуй!')

# print()

# # Создание пустого списка для хранения пришельцев.
# aliens = []
# # Создание 30 зеленых пришельцев.
# for alien_number in range(30):
# 	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# 	aliens.append(new_alien)

# for alien in aliens[0:3]:
# 	if alien['color'] == 'green':
# 		alien['color'] = 'yellow'
# 		alien['speed'] = 'medium'
# 		alien['points'] = 10
# 	elif alien['color'] == 'yellow':
# 		alien['color'] = 'red'
# 		alien['speed'] = 'fast'
# 		alien['points'] = 15
#
# # Вывод первых 5 пришельцев:
# for alien in aliens[0:5]:
# 	print(alien)
# print("...")
# # Вывод количества созданных пришельцев.
# print(f"Total number of aliens: {len(aliens)}")

# message = input('Скажи мне что-нибудь, и я скажу это в ответ: ')
# print(message)
#
# name = input('Пожалуйста, введите своё имя: ')
# print(f"\nHello, {name}!")
#
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# height = input("How tall are you, in inches? ")
# height = int(height)
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
#
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)
# if number % 2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")

# promt = ('Автомобиль какой марки вы ищите?' )
# car = input(promt)
# print('Давайте посмотрим, могу ли я найти для вас' + car)
# answer = input('На сколько человек вы хотите забронировать столик?')
# answer = int(answer)
# # print(answer)
# if answer <= 8:
#     print('Ваш столик готов!')
# else:
#     print('К сожалению, вам придётся подождать')

# number = input('Введите, пожалуйста, число')
# number = int(number)
# if number % 2 == 0:
#     print('Ваше число', number, 'чётное')
# else:
#     print('Ваше число', number, 'нечётное')

# number = input('Введите, пожалуйста, число')
# number = int(number)
# if number % 10:
#     print('Ваше число', number, 'не делится на 10')
# else:
#     print('Ваше число', number, 'делится на 10')

# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# prompt = '\nВыберите дополнение для пиццы.'
# prompt += '\nДля выхода напишите слово "выход". '
# while True:
#     message = input(prompt)
#     if message == 'выход':
#         #break
#         print('Вы вышли из заказа.')
#     else:
#         print('Выше дополнение добавлено к пицце.')

# prompt = '\nПожалуйста, введите ваш возраст цифрой.'
# prompt += '\nДля выхода напишите слово "выход". '
# active = True
# while active:
#     age = input(prompt)
#     if age == 'выход':
#         active = False
#     elif int(age) <= 3:
#         print('Ваш билет бесплатный.')
#     elif int(age) > 3 and int(age) <= 12:
#         print('Ваш билет стоит 250 рублей.')
#     elif int(age) > 12:
#         print('Ваш билет стоит 350 рублей.')
#     else:
#         break

# a = 4
# while a < 5:
#     print('Бесконечный цикл.')

# prompt = '\nПожалуйста, выберите дополнение для пиццы.'
# prompt += '\nНапишите "выход", если хотите отказаться. '
# message = ''
# while message != 'выход':
#     message = input(prompt)
#     # message = ('\nВаш заказ дополнен.')
#     print('Ваш заказ дополнен.')
#     if message == 'выход':
#         print('Вы вышли.')
#         break

# age = input('\nВведите ваш возраст в цифрах: ')
# active = True
# while active:
#     if int(age) < 3:
#         print('Ваш билет бесплатный.')
#         break
#     elif int(age) >= 3 and int(age) < 12:
#         print('Ваш билет стоит 10 долларов')
#         break
#     elif int(age) >= 12:
#         print('Ваш билет стоит 15 долларов.')
#         break

# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print('Проверка пользователя: ', current_user.title())
#     confirmed_users.append(current_user)
#
# print('\nСледующие пользователи был подтверждены: ')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
#
# print()
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
#
# print()

# sandwich_orders = ['сыр', 'pastrami', 'говядина', 'pastrami', 'курица', 'свинина', 'pastrami', 'тунец']
# finished_sandwiches = []
# print('К сожалению, пастрами больше нет.')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)
#
# while sandwich_orders:
#     sandwich_order = sandwich_orders.pop()
#     print('Я сделаю вам ' + sandwich_order + ' сэндвич')
#     finished_sandwiches.append(sandwich_order)
#
# print('Готовые сэндвичи с: ')
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)
#
# while 'pastrami' in finished_sandwiches:
#     finished_sandwiches.remove('pastrami')
# print(finished_sandwiches)

def greet_user(username):
    # Выводит простое приветствие."""
    print('Hello,', username + '!')


greet_user('Олег')


def display_message():
    print('В этой теме рассматриваются функции.')


display_message()


def favorite_book(title):
    print('Одна из моих любимых книг - ', title + '.')


favorite_book('Маленькая жизнь')

print()


def describe_pet(animal_type, pet_name):
    # Выводит информацию о животном."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')


def make_shirt(size, text):
    print('\nРазмер этой футболки: ', size, )
    print('Текст на этой футболке: ', text)


make_shirt('46', 'Какая крутая футболка!')
make_shirt(text='Новый крутой текст!', size='48')


def make_shirt(size='S', text='I love Python'):
    print('\nРазмер этой футболки: ', size, )
    print('Текст на этой футболке: ', text)


make_shirt()

print()


def describe_city(city, country='Россия'):
    print(city, 'находится в', country)


describe_city('Москва')
describe_city('Хабаровск')
describe_city('Санья', 'Китай')

print()

def get_formatted_name(first_name, last_name, middle_name = ''):
    # full_name = f'{first_name} {middle_name} {last_name}'
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name):
    person = {'first' : first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    person = {'first' : first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# def get_formatted_name(first_name, last_name):
# #Возвращает аккуратно отформатированное полное имя."""
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()
#
# while True:
#     print('\nНапишите, пожалуйста, своё имя: ')
#     print('(напишите "выход", чтобы выйти)')
#
#     f_name = input('Имя: ')
#     if f_name == 'выход':
#         break
#     l_name = input('Фамилия: ')
#     if l_name == 'выход':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f'\nПривет, {formatted_name}!')

print()

def city_country(city, country):
    full_name = city + ', ' + country
    return full_name.title()

a = city_country('santiago', 'chile')
print(a)

def city_country3(city3, country3):
    a3 = city3 + ', ' + country3
    return a3.title()

x = city_country3('калининград', 'россия')
x = city_country3('владивосток', 'россия')
x = city_country3('санья', 'китай')
print(x)

print()












































