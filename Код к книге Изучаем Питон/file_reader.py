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

print()

filename = 'pi_digits.txt'
with open(filename) as file_object:
    #lines = file_object.read()
    for line in file_object:
        #line.replace('file', 'dfg')
        print(line.rstrip())

    message = 'file.'
    message.replace('file', 'cat')

    print(message)

message = "I really like dogs."
message.replace('dogs', 'cats')
print(message)



