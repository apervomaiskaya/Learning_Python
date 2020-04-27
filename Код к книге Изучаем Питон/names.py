# from name_function import get_formatted_name
# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#     middle = input("Please give me a middle name: ")
#     if middle == 'q':
#         break
#
#     formatted_name = get_formatted_name(first, last)
#     print('\tNeatly formatted name: ' + get_formatted_name(first, middle, last))

from name_function import get_formatted_name1

print('Напишите "в", чтобы выйти')
while True:
    first = input('Введите ваше имя: ')
    if first == 'в':
        break
    last = input('Введите вашу фамилию: ')
    if last == 'в':
        break

    formatted_name1 = get_formatted_name1(first, last)
    print('Привет, ' + get_formatted_name1(first, last) + '!')