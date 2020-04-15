# with open('E:\Другие загрузки\Обучение\Код к книге Изучаем Питон\pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.strip())

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# for line in lines:
#     print(line.rstrip())
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# print(pi_string)
# print(len(pi_string))
#
# filename = 'E:\Другие загрузки\Обучение\Код к книге Изучаем Питон\ehmatthes-pcc_2e-9e7977b\chapter_10\pi_million_digits.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(f"{pi_string[:5552]}...")
# print(len(pi_string))
# birthday = input("Enter your birthday, in the form ddmmyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")

# with open('E:\Другие загрузки\Обучение\Код к книге Изучаем Питон\ehmatthes-pcc_2e-9e7977b\chapter_10\pi_million_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents)
# print(len(contents))

# print()
#
# filename = 'E:\Другие загрузки\Обучение\Код к книге Изучаем Питон\pi_digits.txt'
# with open('E:\Другие загрузки\Обучение\Код к книге Изучаем Питон\pi_digits.txt') as file_object:
#     for line in file_object:
#         print(line.strip())

# print()
#
# filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     #lines = file_object.read()
#     for line in file_object:
#         #line.replace('file', 'dfg')
#         print(line.rstrip())
#
#     message = 'file.'
#     message.replace('file', 'cat')
#
#     print(message)

# message = 'I really like dogs.'
# message.replace('dogs', 'cats')
# print(message)

# filename = 'programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write('Я люблю программировать!')

# filename = 'programming.doc'
#
# with open(filename, 'w') as file_object:
#     file_object.write('48 dgd I love programming!, Я люблю программировать!\n')
#     file_object.write('45 ghe I love programming!, Я люблю программировать!\n')
#
# with open(filename, 'a') as file_object:
#     file_object.write('Также я люблю искать значения в наборах данных.\n')
#
# filename = 'programming.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write('48 dgd I love programming!, Я люблю программировать!\n')
#     file_object.write('45 ghe I love programming!, Я люблю программировать!\n')
#
# with open(filename, 'a') as file_object:
#     file_object.write('Также я люблю искать значения в наборах данных.\n')

# prompt = 'Если хотите закончить, напишите "выход"'
# prompt = 'Как ваше имя? '
# active = True
# while active:
#     message = input(prompt)
#     if message == 'выход':
#         active = False
#     else:
#         print('Привет,', message.title() + '!')
#         with open('guest_book.txt', 'a') as file_object:
#             file_object.write(message.title())
#             file_object.write(', рады вас видеть!\n')

prompt = 'Если хотите закончить, напишите "выход"'
prompt = 'Почему вам нравится программировать? '
active = True
while active:
    message = input(prompt)
    if message == 'выход':
        active = False
    else:
        print('Вам нравится программировать, потому что', message)
        with open('pool.txt', 'a') as file_object:
            file_object.write(message)
            file_object.write('\n')















































































































































