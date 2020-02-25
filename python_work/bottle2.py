Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================ RESTART: E:\Другие загрузки\Обучение\bottle1.py ===============
Bottle v0.12.18 server starting up (using WSGIRefServer())...
Listening on http://localhost:9999/
Hit Ctrl-C to quit.

127.0.0.1 - - [25/Dec/2019 19:46:21] "GET / HTTP/1.1" 200 37
127.0.0.1 - - [25/Dec/2019 19:46:21] "GET /favicon.ico HTTP/1.1" 404 742

======== RESTART: E:\Другие загрузки\Обучение\bottle1.py =======
Bottle v0.12.18 server starting up (using WSGIRefServer())...
Listening on http://localhost:9999/
Hit Ctrl-C to quit.

>>> from bottle import route, run, static_file
@route('/')
def main():
	return static_file('index.html', root='.')
run(host='localhost', port=9999)
