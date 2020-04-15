try:
    print(5/0)
except ZeroDivisionError:
    print('Вы не можете делить на ноль!')

print()

print("Дайте мне два числа, и я разделю их.")
print('Напишите "выход", чтобы выйти.')

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('Вы не можете делить на ноль!')
    else:
        print(answer)