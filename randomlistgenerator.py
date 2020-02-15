Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import randint
>>> a_length = randint(1,10)
>>> a = []
>>> for i in range(a_length):
	a.append(randint(1,10))
print(a)
SyntaxError: invalid syntax
>>> 
>>> 