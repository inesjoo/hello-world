a=int(input())
for i in range(a):
    for j in range (a+i):
        if j<=a-2-i:
            print(' ',sep='',end='')
        else:
            print('*',sep='',end='')
    print()
