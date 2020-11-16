Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5):
	for j in range (5):
		print('j:',j, sep='',end=' ')
	print('i:',i,'\\n',sep'')
	
SyntaxError: invalid syntax
>>> for i in range(5):
	for j in range (5):
		print('j:',j, sep='',end=' ')
	print('i:',i,'\\n',sep='')

	
j:0 j:1 j:2 j:3 j:4 i:0\n
j:0 j:1 j:2 j:3 j:4 i:1\n
j:0 j:1 j:2 j:3 j:4 i:2\n
j:0 j:1 j:2 j:3 j:4 i:3\n
j:0 j:1 j:2 j:3 j:4 i:4\n
>>> 