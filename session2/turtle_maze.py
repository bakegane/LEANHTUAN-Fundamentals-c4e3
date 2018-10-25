from turtle import *

s = 10
shape ("turtle")
speed (0)
for i in range(100):
    forward(s)
    left(90)
    s += 10
mainloop()