import json
def get_stored_username():
    # Получает хранимое имя пользователя, если оно существует.
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    # Запрашивает новое имя пользователя
    username = input('Как вас зовут? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    # Приветствует пользователя по имени
    username = get_stored_username()
    if username:
        print('С возвращением,', username + '!')
    else:
        username = get_new_username()
        print('Мы вспомним вас, когда вы вернётесь,', username)

greet_user()

import json
filename = 'favorite number.json'

# Здесь загружает любимое число из файла
try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)

# Здесь всё, что связано, если файл не найден
except FileNotFoundError:
    favorite_number = input('Введите ваше любимое число ')

    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print('Ваше любимое число - это', favorite_number + '.')

else:
    print('Я знаю ваше любимое число - это', favorite_number + '.')

























