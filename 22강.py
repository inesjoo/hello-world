Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[10,20,30]
>>> a.append(500)
>>> a
[10, 20, 30, 500]
>>> lens(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lens(a)
NameError: name 'lens' is not defined
>>> len(a)
4
>>> a=[]
>>> a.append(10)
>>> a
[10]
>>> a=[10,20,30]
>>> a.append([500,600])
>>> a
[10, 20, 30, [500, 600]]
>>> len(a)
4
>>> a=[10,20,30]
>>> a.extend([500,600])
>>> a
[10, 20, 30, 500, 600]
>>> len(a)
5
>>> a=[10,20,30]
>>> a.insert(2,500)
>>> a
[10, 20, 500, 30]
>>> len(a)
4
>>> a=[10,20,30]
>>> a.insert(len(a),500)
>>> a
[10, 20, 30, 500]
>>> a.pop()
500
>>> a.pop(1)
20
>>> a
[10, 30]
>>> del a[1]
>>> a
[10]
>>> #pop이랑 del은 비슷해요
>>> a=[10,20,30,40]
>>> a=[10,20,30,20]
>>> a.remove(20)
>>> 
>>> a
[10, 30, 20]
>>> 