import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print('С возвращением,', username + '!')