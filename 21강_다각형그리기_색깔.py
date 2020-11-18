import turtle as t
n=int(input())
t.shape('turtle')
t.color('#823871')
t.begin_fill()

for i in range(n):
    t.forward(100)
    t.rt(360/n)
t.end_fill()
