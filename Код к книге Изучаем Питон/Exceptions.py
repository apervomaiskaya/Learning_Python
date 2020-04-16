try:
    print(5/0)
except ZeroDivisionError:
    print('Вы не можете делить на ноль!')

print()

# print("Дайте мне два числа, и я разделю их.")
# print('Напишите "выход", чтобы выйти.')
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print('Вы не можете делить на ноль!')
#     else:
#         print(answer)

filename = 'cats.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print('Извините,', filename, 'не существует.')

# filename = 'alice.txt'
# with open(filename, 'a') as file_object:
#     file_object.write('Это книга "Алиса в стране чудес"\n')
# #with open(filename, 'a') as file_object:
#     file_object.write('Метод split() разделяет строку')

# prompt = 'Напишите "выход", чтобы выйти'
# while True:
#     first_number = input('Введите первое число: ')
#     if first_number == 'выход':
#         break
#
#     second_number = input('Введите второе число: ')
#     if second_number == 'выход':
#         break
#
#     try:
#         answer = int(first_number) + int(second_number)
#         print(answer)
#
#     except ValueError:
#         print('Вы можете вводить только цифры')

# ЧИТАЮ СОДЕРЖИМОЕ ДВУХ ФАЙЛОВ! КРУТО!
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents)
            print()

    except FileNotFoundError:
        print('Файл', filename, 'не найден')






































