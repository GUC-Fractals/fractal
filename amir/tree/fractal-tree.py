from turtle import *

def draw(angle, size, levels):
    if levels==0:
        color("green")
        dot(size)
        return
    
    forward(size)
    right(angle)
    draw(angle, size*0.8, levels-1) # right branch

    left(angle*2)
    draw(angle, size*0.8, levels-1) #left branch

    right(angle)
    backward(size)


left(90)
draw(30, 70, 7)


