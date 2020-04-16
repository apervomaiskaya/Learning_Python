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

# ЧАСТОТНОСТЬ СЛОВА "the"
filename = 'Meine erste Weltreise.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Подсчет приблизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    line1 = contents.count('the ')
    line2 = contents.count('the')
    print('Количество слова "the " равно: ', line1)
    print('Количество слова "the" равно: ', line2)
    print(f"The file {filename} has about {num_words} words.")
    print(int(line2) - int(line1))









































