from turtle import *

def instructions(levels,size):
    right(15)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size*0.99)
    right(90)
    forward(size*0.99)
    right(90)
    draw(levels-1,size*0.88)

def draw(levels,size):

    if levels == 0:
        return
    instructions(levels,size)


left(90)
draw(100,200)
mainloop()

