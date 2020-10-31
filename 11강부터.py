Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[0,10,20,30,40,50,60,70,80,90,]
>>> 30 in a
True
>>> 100 in a
False
>>> 100 not in a
True
>>> 43 in (38,76,43,62,19)
True
>>> 1 in range(10)
True
>>> 'P'in'Hello, Python'
True
>>> a=[0,10,20,30]
>>> b=[9,8,7,6]
>>> a+b
[0, 10, 20, 30, 9, 8, 7, 6]
>>> range(0,10)+range(10,20)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    range(0,10)+range(10,20)
TypeError: unsupported operand type(s) for +: 'range' and 'range'
>>> list(range(0,10))+list(range(10,20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> tuple(range(0,10))+tuple(range(10,20))
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
>>> 'Hello'+'world'
'Helloworld'
>>> [0,10,20,30]*2
[0, 10, 20, 30, 0, 10, 20, 30]
>>> [0,10,20,30]*0
[]
>>> list(range(0,5,2))*3
[0, 2, 4, 0, 2, 4, 0, 2, 4]
>>> 'Hello'*3
'HelloHelloHello'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=[0,10,20,30,40,50,60,70,80,90]
>>> len(a)
10
>>> a=['kor','end','mat']
>>> len(a)
3
>>> b=(38,76,43,62,19)
>>> len(b)
5
>>> 