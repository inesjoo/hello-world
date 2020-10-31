Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=10
>>> if x==10:
	    print('10입니다.')

	    
10입니다.
>>> print('if조건문 다음에는 들여쓰기를 해야한다. 하지않으면 오류가 생길것이다. idle에서는 if다음에 자동으로 들여쓰기를 해주지만, 명령프롬프트에서 실행할 경우 자동으로 해주지 않기 때문에 반드시 들여쓰기를 해주어야한다.')
if조건문 다음에는 들여쓰기를 해야한다. 하지않으면 오류가 생길것이다. idle에서는 if다음에 자동으로 들여쓰기를 해주지만, 명령프롬프트에서 실행할 경우 자동으로 해주지 않기 때문에 반드시 들여쓰기를 해주어야한다.
>>> if x=10:
	
SyntaxError: invalid syntax
>>> if x==10:
	print('10입니다')

	
10입니다
>>> 
>>> 
>>> 
>>> 
>>> if 조건문에서 코드를 생략하기
SyntaxError: invalid syntax
>>> x=10
>>> if x==10:
	pass

>>> if x==10:
	pass  #todo:뭔가 넣어야함

>>> 
========================== RESTART: C:/Users/TETRA/Desktop/if_indent_error.py =========================
x에 들어있는 숫자는
10입니다
>>> if 뒤에 명령어 들어쓰기 맞춰줘야
SyntaxError: invalid syntax
>>> 
========================== RESTART: C:/Users/TETRA/Desktop/if_indent_error.py =========================
x에 들어있는 숫자는
10입니다
>>> 
========================== RESTART: C:/Users/TETRA/Desktop/if_indent_error.py =========================
10입니다
>>> if 뒤에 들여쓰기가 맞춰져 있는 것만 같은 if의 명령을 받음 ㅇㅋ?
SyntaxError: invalid syntax
>>> 
========================== RESTART: C:/Users/TETRA/Desktop/if_indent_error.py =========================
>>> 
========================== RESTART: C:/Users/TETRA/Desktop/if_indent_error.py =========================
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: C:/Users/TETRA/Desktop/if_if.py ==============================
10이상입니다.
15입니다.
>>> 
>>> 
>>> 
>>> 
>>> 
============================= RESTART: C:/Users/TETRA/Desktop/if_input.py =============================
10
10입니다.
>>> 
============================= RESTART: C:/Users/TETRA/Desktop/if_input.py =============================
20
20입니다.
>>> 
============================= RESTART: C:/Users/TETRA/Desktop/if_input.py =============================
15
>>> 
============================= RESTART: C:/Users/TETRA/Desktop/if_input.py =============================
11.11
Traceback (most recent call last):
  File "C:/Users/TETRA/Desktop/if_input.py", line 1, in <module>
    x=int(input())
ValueError: invalid literal for int() with base 10: '11.11'
>>> 